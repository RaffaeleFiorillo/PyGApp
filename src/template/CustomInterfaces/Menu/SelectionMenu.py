from src.template.CustomWidgets.ProjectButton import ProjectButton
from src.template.CustomInterfaces import BasicInputManager
from pygame import Surface
import pygame
from pathlib import Path
import os
from src.app_config import SCREEN_WIDTH
from src.session_state import SessionState
from src.template.CustomWidgets.MapWidget import Map
from src.template.CustomWidgets.MapProject import MapProject



class SelectionMenu(BasicInputManager):
    link = "SelectEdit"

    def __init__(self, screen, buttons: [ProjectButton]):
        super().__init__(screen, buttons)

    @staticmethod
    def create_buttons(projects_directory, for_folder, file_extension) -> [ProjectButton]:
        if for_folder:
            labels = [name for name in os.listdir(projects_directory) if os.path.isdir(os.path.join(projects_directory, name))]
        else:
            labels = [file.name for file in Path(projects_directory).glob(f"*.{file_extension}")]
        font_size = 30
        font = pygame.font.Font(None, font_size)
        surface_labels = [font.render(label, True, (255, 255, 255)) for label in labels]
        buttons = [ProjectButton(SCREEN_WIDTH*0.0675, 30+(font_size+30)*i, surface_labels[i], labels[i]) for i in range(len(labels))]

        return buttons

    @staticmethod
    def create_menu(screen, directory, for_folder=False, file_extension="pickle"):
        # audio.stop_all_sounds()
        # audio.play(change_menu_sound)
        buttons = SelectionMenu.create_buttons(directory, for_folder, file_extension)
        menu = SelectionMenu(screen, buttons)
        return menu

    def start(self):
        background = Surface(self.screen.get_size())
        background.convert().fill((0, 0, 0))
        while True:
            self.clock.tick(30)
            # effect carries information about what to do based on input. None is base case and means "do nothing"
            effect = self.manage_events()  # taking and evaluating input
            if effect is not None:  # if meaningful input is given take respective action
                return effect
            if not self.already_checked_cursor:  # saves time avoiding iterating over buttons when it was done already
                self.cursor_is_on_button()  # mouse visual interaction with interface
            self.refresh(background)

    def set_button_to_active(self, new_active_code: int):
        if new_active_code != self.active_code:
            # audio.play(self.button_activation_sound)
            self.button_list[self.active_code].is_active = False
            self.active_code = new_active_code

    def enter_action(self):
        if self.active_code is not None:
            map_file_name = self.button_list[self.active_code].project_directory
            SessionState.map = Map.load_from_txt(map_file_name)
            SessionState.project = MapProject(SessionState.map.project_name)
            return "Edit"
        return "MainMenu"

    def refresh(self, background: Surface):
        self.screen.blit(background, (0, 0))
        [button.draw(self.screen) for button in self.button_list]
        pygame.display.update()

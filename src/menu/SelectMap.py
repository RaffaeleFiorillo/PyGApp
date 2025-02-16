from src.template.CustomInterfaces.Menu.SelectionMenu import SelectionMenu
from src.template.CustomWidgets.ProjectButton import ProjectButton
import pygame
from pathlib import Path
from src.app_config import SCREEN_WIDTH
from src.template.CustomWidgets.MapWidget import Map
from src.template.CustomWidgets.MapProject import MapProject
from src.session_state import SessionState


class SelectMap(SelectionMenu):
    link = "SelectMap"

    def __init__(self, screen, buttons):
        super().__init__(screen, buttons)

    @staticmethod
    def create_buttons(projects_directory) -> [ProjectButton]:
        labels = ["New Map"] + [file.name for file in Path(projects_directory).glob(f"*.pickle")]
        font_size = 30
        font = pygame.font.Font(None, font_size)
        surface_labels = [font.render(label, True, (255, 255, 255)) for label in labels]
        buttons = [ProjectButton(SCREEN_WIDTH*0.0675, 30+(font_size+30)*i, surface_labels[i], labels[i]) for i in range(len(labels))]

        return buttons

    @staticmethod
    def display(screen) -> str:
        buttons = SelectMap.create_buttons("assets/maps")
        menu = SelectMap(screen, buttons)
        # menu.button_list.append()
        next_link = menu.start()
        return next_link

    def enter_action(self):
        if self.active_code == 0:
            return "CreateMap"
        elif self.active_code > 0:
            map_file_name = self.button_list[self.active_code].project_directory
            SessionState.map = Map.load_from_pickle(map_file_name)
            SessionState.project = MapProject(SessionState.map.project_name)
        return "Edit" if self.active_code > 0 else "MainMenu"

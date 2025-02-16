from src.template.CustomInterfaces.Menu.BasicInputManager import BasicInputManager
from src.template.CustomWidgets.MainMenuButton import MainMenuButton
import pygame
from pygame import Surface
from pygame.event import Event
from src.pygapp.utils import graphics as grp
from src.app_config import SCREEN_WIDTH, SCREEN_HEIGHT


# provides a simple structure for a menu. The Main Menu directly uses it
class BaseMenu(BasicInputManager):
    def __init__(self, screen: Surface, direct: str, buttons: [MainMenuButton]):
        super().__init__(screen, buttons)
        self.screen = screen  # screen surface
        self.name = direct.split("/")[-1][:-4]  # the name of the menu (extracted from its directory)

        self.menu_image = grp.load_image(direct)  # image of the menu's background (loaded based on its name)
        menu_image_size = self.menu_image.get_size()
        self.menu_image_display_coo = ((SCREEN_WIDTH-menu_image_size[0])//2, (SCREEN_HEIGHT-menu_image_size[1])//2)

        self.navigation_image = grp.load_image(f"menu/interfaces/navigation/navigation.png")  # img with info about menu
        self.info_images = [grp.load_image(f"menu/info/info_{self.name}/{i + 1}.png") for i, _ in enumerate(buttons)]
        self.active_code = 0  # index of the active button
        self.current_frame = 0  # frame representing the current state of the button's evidencing effect

    @staticmethod
    def create_buttons(button, button_dir: str, effects: [str], y_coo=None):
        position_x = (SCREEN_WIDTH - 260) // 2
        position_y = y_coo if y_coo is not None else [y for y in range(100, 600, 120)]
        buttons = []
        for i, y in enumerate(position_y[:len(effects)]):
            directory = f"{button_dir}/{i + 1}.png"
            buttons.append(button(position_x, y, directory, effects[i]))
        return buttons

    def get_effect_rect(self) -> (int, int, int, int):
        adjust = self.current_frame*2
        x = int(self.button_list[self.active_code].x-adjust)
        y = int(self.button_list[self.active_code].y-adjust)
        le = int(self.button_list[self.active_code].width+adjust*2)
        hi = int(self.button_list[self.active_code].height+adjust*2)
        return x, y, le, hi

    def draw_buttons(self):
        pygame.draw.rect(self.screen, (0, 0, 255), self.get_effect_rect(), 3)
        [but.draw(self.screen) for but in self.button_list]  # draw each button
        self.button_list[self.active_code].draw_info(self.screen)  # displays information about current active button
        self.current_frame = (self.current_frame + 0.25) % 3  # update frame in a way that it restarts at a value of 3

    def update_coord_effect(self):
        return self.button_list[self.active_code].x - 12, self.button_list[self.active_code].y - 12

    def get_effect_by_input(self, event: Event = None):
        effect = super().get_effect_by_input(event)
        return effect

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

    def manage_buttons(self, event: Event):
        new_active_code = self.active_code  # go up if value is -1 and down if it's 1
        if event.key == pygame.K_UP:
            new_active_code -= 1
        elif event.key == pygame.K_DOWN:
            new_active_code += 1
        elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
            return self.enter_action()
        new_active_code = new_active_code % len(self.button_list)  # make sure active_code doesn't go off-boundaries
        self.set_button_to_active(new_active_code)

    def refresh(self, background: Surface):
        self.screen.blit(background, (0, 0))
        self.screen.blit(self.menu_image, self.menu_image_display_coo)
        self.screen.blit(self.navigation_image, (355, 600))
        self.draw_buttons()
        self.screen.blit(self.info_images[self.active_code], (786, 195))
        pygame.display.update()

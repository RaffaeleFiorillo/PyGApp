import pygame
from pygame import Surface
from pygame.event import Event
from src.pygapp.utils import graphics as grp
from src.template.CustomInterfaces import BasicInputManager
from src.template.CustomWidgets.MainMenuButton import MainMenuButton


class Exit(BasicInputManager):
    link = "Exit"

    def __init__(self, screen: Surface, buttons: [MainMenuButton]):
        super().__init__(screen, buttons)
        self.navigation_image = grp.load_image(f"menu/interfaces/navigation/navigation2.png")
        self.name_image = grp.load_image("menu/interfaces/exit.png")
        self.effect = [grp.load_image(f"menu/effects/1/{i+1}.png") for i in range(4)]
        self.buttons_effect_coo = {0: (240, 410), 1: (567, 410)}
        self.active_code = 0
        self.screen = screen
        self.current_frame = 0

    @staticmethod
    def display(screen) -> str:
        # audio.play(exit_sound)
        buttons = [
            MainMenuButton(240, 410, f"menu/buttons/3/1.png", False),
            MainMenuButton(580, 410, f"menu/buttons/3/2.png", True)
        ]
        mapp_maker_interface = Exit(screen, buttons)
        next_link = mapp_maker_interface.start()
        return next_link

    def start(self) -> str:
        while True:
            self.clock.tick(30)
            effect = self.manage_events()
            if effect is not None:
                return effect
            if not self.already_checked_cursor:  # saves time avoiding iterating over buttons when it was done already
                self.cursor_is_on_button()  # mouse visual interaction with interface
            self.refresh()

    def manage_buttons(self, event: Event):
        new_active_code = self.active_code  # go up if value is -1 and down if it's 1
        if event.key == pygame.K_RIGHT:
            new_active_code += 1
        elif event.key == pygame.K_LEFT:
            new_active_code -= 1
        elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
            return self.button_list[self.active_code].effect
        new_active_code = new_active_code % len(self.button_list)  # make sure active_code doesn't go off-boundaries
        self.set_button_to_active(new_active_code)

    def update_coord_effect(self):
        self.coord_effect = self.buttons_effect_coo[self.active_code]

    def draw_buttons(self):
        self.screen.blit(self.effect[int(self.current_frame)], self.buttons_effect_coo[self.active_code])
        self.current_frame = (self.current_frame + 0.25) % 3

    def refresh(self):
        self.screen.blit(self.name_image, (0, 0))
        self.draw_buttons()
        self.screen.blit(self.navigation_image, (350, 600))
        pygame.display.update()

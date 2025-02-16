from src.pygapp.widget.BaseWidget import BaseWidget
from src.template.CustomWidgets.ActionButton import ActionButton
from src.app_config import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame import Surface
import pygame


class ActionArea(BaseWidget):
    def __init__(self):
        super().__init__(0, 0, SCREEN_WIDTH * 0.76, SCREEN_HEIGHT * 0.05)
        self.save_button = ActionButton(0, 1, "save")
        self.export_button = ActionButton(35, 1, "export")
        self.delete_button = ActionButton(70, 1, "delete")
        self.exit_button = ActionButton(self.width-40, 1, "menu")

        self.buttons = [self.save_button, self.export_button, self.delete_button, self.exit_button]
        [button.cursor_is_inside((0, 0)) for button in self.buttons]  # displays the buttons upon start

    def update(self) -> str:
        mouse_coo = pygame.mouse.get_pos()
        active_buttons_indexes = [i for i, button in enumerate(self.buttons) if button.cursor_is_inside(mouse_coo)]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Exit"
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                return self.buttons[active_buttons_indexes[0]].action if len(active_buttons_indexes) > 0 else ""
        return ""

    def refresh(self, screen: Surface):
        pygame.draw.rect(screen, (50, 50, 50), (self.x, self.y, self.width, self.height))
        [button.draw(screen) for button in self.buttons]

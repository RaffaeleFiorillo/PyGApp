from src.pygapp.utils import graphics as grp
from src.pygapp.widget.BaseWidget import BaseWidget
import pygame


class ActionButton(BaseWidget):
    base_directory = "menu/buttons/Actions"

    def __init__(self, x: int, y: int, action: str):
        self.image = grp.load_image(f"{self.base_directory}/{action}.png")
        super().__init__(x, y, self.image.get_size()[0], self.image.get_size()[1])
        self.border_color = (0, 0, 0)
        self.is_active = False
        self.action = action

    def cursor_is_inside(self, cursor_coo) -> bool:
        self.is_active = super().cursor_is_inside(cursor_coo)
        self.border_color = (255-255*self.is_active, 255, 255)
        return self.is_active

    def draw(self, screen):
        pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height))
        screen.blit(self.image, (self.x, self.y))

from pygame import Surface
from src.pygapp.utils import graphics as grp
import pygame
from .BaseButton import BaseButton


class MainMenuButton(BaseButton):
    pointer_image = grp.load_image("menu/info/pointer.png")

    def __init__(self, x: int, y: int, directory: str, effect):
        self.image = grp.load_image(directory) if directory != "" else None
        super().__init__(x, y, self.image.get_size()[0], self.image.get_size()[1])
        self.effect = effect

    def draw(self, screen: Surface):
        screen.blit(self.image, (self.x, self.y))

    def draw_info(self, screen):
        screen.blit(self.pointer_image, (685, self.y + self.height // 2 - 19))  # draw the head of the arrow (pointer)
        # line from pointer to center line (vertical)
        pygame.draw.line(screen, (0, 255, 255), (730, self.y + self.height // 2 + 3), (730, 343), 5)
        # center line (horizontal)
        pygame.draw.rect(screen, (0, 255, 255), (728, 342, 60, 5))

    def change_image(self, directory: str):
        self.image = grp.load_image(directory)

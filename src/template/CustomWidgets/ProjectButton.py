from pygame import Surface
import pygame
from .BaseButton import BaseButton
from src.app_config import SCREEN_WIDTH


class ProjectButton(BaseButton):
    base_image_normal = pygame.Surface((SCREEN_WIDTH*0.85, 50))
    base_image_normal.fill((0, 155, 155))
    pygame.draw.rect(base_image_normal, (0, 0, 0), (0, 0, base_image_normal.get_size()[0], base_image_normal.get_size()[1]), 2)

    base_image_active = pygame.Surface((SCREEN_WIDTH*0.85, 50))
    base_image_active.fill((0, 190, 255))
    pygame.draw.rect(base_image_active, (0, 0, 0), (0, 0, base_image_active.get_size()[0], base_image_active.get_size()[1]), 2)

    def __init__(self, x: int, y: int, label: pygame.Surface, project_directory: str):
        self.image = self.base_image_normal
        super().__init__(x, y, self.image.get_size()[0], self.image.get_size()[1])
        self.project_directory = project_directory  # directory with the data for the project to use
        self.label = label  # image with the label of the button

    def draw(self, screen: Surface):
        screen.blit(self.base_image_active if self.is_active else self.base_image_normal, (self.x, self.y))
        screen.blit(self.label, (self.x+10, self.y+20))

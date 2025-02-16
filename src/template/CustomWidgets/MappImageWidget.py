import pygame.image
from src.pygapp.widget import BaseWidget


class MappImage(BaseWidget):
    def __init__(self, image_path):
        self.image_path = image_path
        self.image: pygame.Surface
        super.__init__()

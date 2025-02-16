from src.pygapp.widget.BaseWidget import BaseWidget
from src.template.CustomWidgets.ActionButton import ActionButton
from src.template.CustomWidgets.DropDown import DropDown
from src.app_config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.session_state import SessionState
from pygame import Surface
import pygame
import os
import importlib.util


class ParametersArea(BaseWidget):
    def __init__(self):
        super().__init__(SCREEN_WIDTH*0.76, 0, SCREEN_WIDTH*0.242, SCREEN_HEIGHT)
        self.project = SessionState.project
        self.method = "cellular_automata.py"
        self.folder_path = "assets/generation_methods"
        self.generation_methods = self.get_methods()
        self.generation_method = None
        self.method_dropdown = DropDown(self.x+2, 0, self.width-4, SCREEN_HEIGHT*0.05, self.generation_methods)
        self.generator_button = ActionButton(self.x+30, self.y+40, "generate")

    def get_methods(self) -> list[str]:
        """Returns a list of all python files inside the folder_path."""
        return [f for f in os.listdir(self.folder_path) if f.endswith(".py")]

    def update(self) -> str:
        mouse_coo = (0, 0)
        self.generation_method = None
        self.generator_button.cursor_is_inside(mouse_coo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Exit"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_coo = pygame.mouse.get_pos()
                if self.method_dropdown.cursor_is_inside(mouse_coo):
                    self.method_dropdown.is_active = not self.method_dropdown.is_active
                elif self.generator_button.cursor_is_inside(mouse_coo):
                    self.generation_method = self.get_generation_method()

        if self.method_dropdown.update_options(mouse_coo):
            self.method = self.method_dropdown.value()

        return ""

    def get_generation_method(self):
        file_path = f"assets/generation_methods/{self.method}"

        spec = importlib.util.spec_from_file_location(self.method.split(".")[0], file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.method

    def refresh(self, screen: Surface):
        pygame.draw.rect(screen, (30, 30, 30), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)
        self.generator_button.draw(screen)
        self.method_dropdown.draw(screen)
        pygame.display.update()

from src.pygapp.widget.BaseWidget import BaseWidget
from src.app_config import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame import Surface
import pygame
from src.template.CustomWidgets.MapWidget import Map
from src.session_state import SessionState


class EditArea(BaseWidget):
    def __init__(self):
        super().__init__(0, SCREEN_HEIGHT*0.05, SCREEN_WIDTH*0.76, SCREEN_HEIGHT*0.95)
        self.project = SessionState.project
        self.map: Map = SessionState.map
        self.map.x = self.x+(self.width-self.map.width)//2    # center the map horizontally
        self.map.y = self.y+(self.height-self.map.height)//2  # center the map vertically
        self.map_movement_step: float = 1  # speed of the map when keys are pressed to move it
        self.movement_map = {
            pygame.K_RIGHT: (-1, 0),
            pygame.K_LEFT: (1, 0),
            pygame.K_DOWN: (0, -1),
            pygame.K_UP: (0, 1)
        }

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                tile_coo = self.map.get_cell_coordinates(pygame.mouse.get_pos())
                if tile_coo is not None:
                    if event.button == 1 and self.project.active_tile_image is not None:
                        self.map.add_tile(tile_coo, self.project.active_tile_name, self.project.active_tile_image)
                    elif event.button == 3:
                        self.map.remove_tiles(tile_coo)

        keys = pygame.key.get_pressed()
        # Move Right only if the left side of the map is out of view
        if keys[pygame.K_RIGHT] and self.map.x < self.x:
            self.map.x += self.map_movement_step

        # Move Left only if the right side of the map is out of view
        elif keys[pygame.K_LEFT] and self.map.x + self.map.width > self.x + self.width:
            self.map.x -= self.map_movement_step

        # Move Down only if the top side of the map is out of view
        if keys[pygame.K_DOWN] and self.map.y < self.y:
            self.map.y += self.map_movement_step

        # Move Up only if the bottom side of the map is out of view
        elif keys[pygame.K_UP] and self.map.y + self.map.height > self.y + self.height:
            self.map.y -= self.map_movement_step

    def refresh(self, screen: Surface):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        self.map.display(screen)

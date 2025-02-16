from src.pygapp.widget.BaseWidget import BaseWidget
from src.template.CustomWidgets.DropDown import DropDown
from src.app_config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.session_state import SessionState
from pygame import Surface
import pygame


class AssetArea(BaseWidget):
    def __init__(self, project_directory):
        super().__init__(SCREEN_WIDTH*0.76, 0, SCREEN_WIDTH*0.242, SCREEN_HEIGHT)
        self.project = SessionState.project
        self.category = self.project.categories[0]

        self.tiles = self.project.load_category_tiles(self.category)
        self.tile_size = SessionState.map.tile_size
        self.tile_spacing = 0
        self.tiles_columns = max(2, self.width*0.96 // self.tile_size)  # Fit surfaces in rows
        self.tiles_coordinates = self.generate_tiles_coordinates()
        self.hoover_tile_index = 0
        self.active_tile_index = None
        self.active_rect = (0, 0, 0, 0)
        self.hoover_rect = (0, 0, 0, 0)

        self.category_dropdown = DropDown(self.x+2, 0, self.width-4, SCREEN_HEIGHT*0.05, self.project.categories)

    def generate_tiles_coordinates(self) -> [(int, int)]:
        coo = []

        # Calculate spacing
        total_tile_width = self.tile_size * self.tiles_columns
        remaining_space = (self.width * 0.96) - total_tile_width
        self.tile_spacing = remaining_space // (self.tiles_columns + 1)  # Equal gaps between tiles

        for index, surface in enumerate(self.tiles):
            col = index % self.tiles_columns
            row = index // self.tiles_columns

            # Adjust position with gap
            pos_x = self.x + 5 + (col * self.tile_size) + ((col + 1) * self.tile_spacing)
            pos_y = self.y + 40 + (row * self.tile_size) + ((row + 1) * self.tile_spacing)

            coo.append((pos_x, pos_y))
        return coo

    def update_active_tile_index(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if (
            mouse_x < self.x + 3 + self.tile_spacing
                or
            mouse_x > self.x + 5 + (self.tile_size+self.tile_spacing)*self.tiles_columns):
            self.hoover_tile_index = None
            return

        # Calculate column and row index
        col = (mouse_x - self.x - 5) // (self.tile_size + self.tile_spacing)
        row = (mouse_y - self.y - 40) // (self.tile_size + self.tile_spacing)

        # Calculate tile index
        tile_index = row * self.tiles_columns + col

        # Check if the index is within bounds
        if 0 <= tile_index < len(self.tiles):
            self.hoover_tile_index = int(tile_index)
            self.hoover_rect = (self.tiles_coordinates[self.hoover_tile_index][0] - 2,
                           self.tiles_coordinates[self.hoover_tile_index][1] - 2,
                           self.tile_size + 4,
                           self.tile_size + 4)
        else:
            self.hoover_tile_index = None  # No valid tile hovered

    def update(self) -> str:
        mouse_coo = (0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Exit"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_coo = pygame.mouse.get_pos()
                if self.category_dropdown.cursor_is_inside(mouse_coo):
                    self.category_dropdown.is_active = not self.category_dropdown.is_active
                elif self.hoover_tile_index is not None:
                    self.active_tile_index = self.hoover_tile_index
                    self.project.activate_tile(self.category, self.active_tile_index, self.tiles[self.active_tile_index])
                    self.active_rect = (self.tiles_coordinates[self.hoover_tile_index][0] - 2,
                                        self.tiles_coordinates[self.hoover_tile_index][1] - 2,
                                        self.tile_size + 4,
                                        self.tile_size + 4)

        if self.category_dropdown.update_options(mouse_coo):
            self.category = self.category_dropdown.value()
            self.tiles = self.project.load_category_tiles(self.category)
            self.active_rect = (0, 0, 0, 0)

        if not self.category_dropdown.is_active:
            self.update_active_tile_index()

        return ""

    def refresh(self, screen: Surface):
        pygame.draw.rect(screen, (30, 30, 30), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)

        if self.active_tile_index is not None:
            pygame.draw.rect(screen, (0, 255, 255), self.active_rect)

        for index, surface in enumerate(self.tiles):
            screen.blit(surface, self.tiles_coordinates[index])

        if self.hoover_tile_index is not None:
            pygame.draw.rect(screen, (0, 150, 255), self.hoover_rect, 2)

        self.category_dropdown.draw(screen)

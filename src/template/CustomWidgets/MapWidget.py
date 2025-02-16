import os
from src.pygapp.widget.BaseWidget import BaseWidget
import pygame
from pygame import Surface
import pickle


class Map(BaseWidget):
    def __init__(self, project_name: str, map_file_name: str, rows: int, columns: int, tile_size: int):
        self.name = map_file_name.split(".")[0]
        self.project_name = project_name
        self.tile_size = tile_size
        self.column_number = columns
        self.row_number = rows

        self.save_file_name = self.name+".pickle"
        self.tiles_coordinates_by_name: {str: [(int, int)]} = {}
        self.tiles_images_by_name: {str: Surface} = {}

        super().__init__(0, 0, self.tile_size*self.column_number, self.tile_size*self.row_number)
        self.grid_lines = []
        self.compute_grid_lines()

    @staticmethod
    def load_from_pickle(map_file_name: str) -> "Map":
        """Loads a Map instance from a pickle file."""
        with open(f"assets/maps/{map_file_name}", "rb") as file:
            data = pickle.load(file)

        # Create a new Map instance
        map_instance = Map(data["project_name"], map_file_name, data["row_number"], data["column_number"], data["tile_size"])

        # The tile images must be reloaded manually after loading the map
        map_instance.tiles_coordinates_by_name = data["tiles_coordinates_by_name"]
        map_instance.tiles_images_by_name = {}  # You need a way to reload images

        return map_instance

    @staticmethod
    def load_from_txt(map_file_name: str) -> "Map":
        """Loads a Map instance from a TXT file."""
        params = {}

        with open(f"assets/maps/{map_file_name}", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                key = key.strip()
                value = value.strip().strip('"')

                # Convert numerical values
                if key in {"rows", "columns", "tile_size"}:
                    value = int(value)

                params[key] = value

        # Create and return a new Map instance
        map_instance = Map(params["project_name"], params["map_name"], params["rows"], params["columns"], params["tile_size"])

        return map_instance

    def save_to_file(self):
        """Saves the map to a file, excluding non-serializable pygame surfaces."""
        data = {
            "tile_size": self.tile_size,
            "column_number": self.column_number,
            "row_number": self.row_number,
            "project_name": self.project_name,
            "tiles_coordinates_by_name": self.tiles_coordinates_by_name  # Exclude images
        }
        with open(f"assets/maps/{self.save_file_name}", "wb") as file:
            pickle.dump(data, file)

    def export_map_as_png(self):
        # Create a transparent surface (with alpha channel)
        map_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        # Draw tiles onto the surface
        for tile_name, tile_image in self.tiles_images_by_name.items():
            for tile_coo in self.tiles_coordinates_by_name[tile_name]:
                map_surface.blit(tile_image, (tile_coo[0] * self.tile_size, tile_coo[1] * self.tile_size))

        map_image_name = f"assets/images/exports/{self.name}.png"
        if os.path.exists(map_image_name):
            counter = 1
            while os.path.exists(map_image_name):
                map_image_name = f"assets/images/exports/{self.name}_{counter}.png"
                counter += 1

        # Save the surface as a PNG
        pygame.image.save(map_surface, map_image_name)

    def delete(self):
        if os.path.exists(f"assets/maps/{self.save_file_name}"):
            os.remove(f"assets/maps/{self.save_file_name}")

    def compute_grid_lines(self):
        # Vertical lines
        y = self.row_number*self.tile_size
        for col_index in range(self.column_number):
            x = col_index * self.tile_size
            self.grid_lines.append(((x, 0), (x, y)))

        x = self.column_number * self.tile_size
        # Horizontal lines
        for row_index in range(self.row_number):
            y = row_index * self.tile_size
            self.grid_lines.append(((0, y), (x, y)))

    def get_cell_coordinates(self, mouse_coo):
        mouse_x, mouse_y = mouse_coo

        # Convert mouse position to grid coordinates
        col = (mouse_x - self.x) // self.tile_size
        row = (mouse_y - self.y) // self.tile_size

        # Ensure the coordinates are within bounds
        if 0 <= col < self.column_number and 0 <= row < self.row_number:
            return int(col), int(row)
        return None  # Return None if out of bounds

    def add_tile(self, tile_coo: (int, int), tile_name: str, tile_image: Surface):
        if tile_name not in self.tiles_coordinates_by_name.keys():
            self.tiles_coordinates_by_name[tile_name] = [tile_coo]
            self.tiles_images_by_name[tile_name] = tile_image
        else:
            self.tiles_coordinates_by_name[tile_name].append(tile_coo)

    def remove_tiles(self, coo: (int, int)):
        for tile_name in self.tiles_images_by_name:
            new_coo = []
            for tile_coo in self.tiles_coordinates_by_name[tile_name]:
                if tile_coo != coo:
                    new_coo.append(tile_coo)
            self.tiles_coordinates_by_name[tile_name] = new_coo

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

        translated_lines = [((x1 + self.x, y1 + self.y), (x2 + self.x, y2 + self.y)) for (x1, y1), (x2, y2) in self.grid_lines]
        [pygame.draw.line(screen, (0, 0, 0), line[0], line[1]) for i, line in enumerate(translated_lines)]
        for tile_name in self.tiles_images_by_name:
            for tile_coo in self.tiles_coordinates_by_name[tile_name]:
                screen.blit(self.tiles_images_by_name[tile_name], (self.x+tile_coo[0]*self.tile_size, self.y+tile_coo[1]*self.tile_size))

import os
from pygame import Surface
from src.pygapp.utils.graphics import load_image


class MapProject:
    def __init__(self, project_name: str):
        self.name = project_name
        self.folder_path: str = f"assets/images/projects/{project_name}"
        self.categories: list[str] = self.get_categories()
        self.tiles_by_category: dict[str, list[str]] = self.get_files_by_category()
        self.active_tile_image: Surface = None
        self.active_tile_name: str = ""
        self.used_tiles_images_by_category: dict[str, dict[str, Surface]] = {}

    def get_categories(self) -> list[str]:
        """Returns a list of all folders (categories) inside the folder_path."""
        return [d for d in os.listdir(self.folder_path) if os.path.isdir(os.path.join(self.folder_path, d))]

    def get_files_by_category(self) -> dict[str, list[str]]:
        """Creates a dictionary mapping each category to a list of its file names."""
        return {
            category: [
                file for file in os.listdir(os.path.join(self.folder_path, category))
                if os.path.isfile(os.path.join(self.folder_path, category, file))
            ]
            for category in self.categories
        }

    def load_tile(self, category: str, file_name: str) -> Surface:
        return load_image(f"projects/{self.name}/{category}/{file_name}")

    def load_category_tiles(self, category: str) -> [Surface]:
        return [load_image(f"projects/{self.name}/{category}/{tile_name}") for tile_name in self.tiles_by_category[category]]

    def activate_tile(self, category: str, active_tile_index: int, image: Surface):
        self.active_tile_name = self.tiles_by_category[category][active_tile_index]
        if category not in self.used_tiles_images_by_category.keys():
            self.used_tiles_images_by_category[category] = {self.active_tile_name: image}
        self.used_tiles_images_by_category[category][self.active_tile_name] = image
        self.active_tile_image = image

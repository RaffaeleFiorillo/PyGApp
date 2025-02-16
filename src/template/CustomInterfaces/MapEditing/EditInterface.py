import pygame
from src.pygapp.interface.BaseInterface import BaseInterface
from src.template.CustomWidgets.EditArea import EditArea
from .AssetArea import AssetArea
from src.template.CustomWidgets.ActionArea import ActionArea


class EditInterface(BaseInterface):
    """
    This interface manages the three areas that allow the user to access the features of the edition process:
        - EditArea:   Where the map is created and edited.
        - AssetArea:  Where the assets for the map are, and can be searched and selected to be used.
        - ActionArea: Buttons that offer different actions to the user (Save, exit, ...).
    This interface only updates the area where actions are being taken. This makes it much more efficient.
    """
    def __init__(self, screen):
        super().__init__(screen, "Edit")
        self.edit_area = EditArea()
        self.asset_area = AssetArea("Cave")
        self.action_area = ActionArea()
        self.areas = [self.edit_area, self.asset_area, self.action_area]
        self.active_area_index = 1
        self.next_link = ""
        self.load_map()

    def load_map(self):
        for category in self.asset_area.category_dropdown.values:
            for tile_name in self.edit_area.map.tiles_coordinates_by_name:
                if tile_name not in self.edit_area.project.tiles_by_category[category]:
                    continue
                image = self.edit_area.project.load_tile(category, tile_name)
                self.edit_area.map.tiles_images_by_name[tile_name] = image

    def start(self) -> str:
        self.edit_area.update()
        self.edit_area.refresh(self.screen)
        self.asset_area.update()
        self.asset_area.refresh(self.screen)
        self.action_area.update()
        self.action_area.refresh(self.screen)

        while True:
            self.update()
            if self.next_link == self.action_area.save_button.action:
                self.edit_area.map.save_to_file()
            elif self.next_link == self.action_area.delete_button.action:
                self.edit_area.map.delete()
                return "MainMenu"
            elif self.next_link == self.action_area.export_button.action:
                self.edit_area.map.export_map_as_png()
            elif self.next_link == self.action_area.exit_button.action:
                return "MainMenu"
            elif self.next_link == "Exit":
                return "Exit"

            self.refresh()

    def update(self):
        mouse_coo = pygame.mouse.get_pos()
        active_area_indexes = [i for i, area in enumerate(self.areas) if area.cursor_is_inside(mouse_coo)]
        self.active_area_index = active_area_indexes[0] if len(active_area_indexes) > 0 else self.active_area_index
        self.next_link = self.areas[self.active_area_index].update()

    def refresh(self):
        [area.refresh(self.screen) for area in self.areas]
        pygame.display.update()

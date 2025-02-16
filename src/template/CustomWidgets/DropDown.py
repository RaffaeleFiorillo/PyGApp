import pygame.draw
from pygame import Surface
from src.pygapp.widget.BaseWidget import BaseWidget
from src.pygapp.utils.graphics import load_image

class DropDown(BaseWidget):
    def __init__(self, x: int, y: int, width: int, height: int, values: [str]):
        super().__init__(x, y, width, height)
        self.label = values[0] if len(values) > 0 else "Empty"
        self.label_images = []
        self.label_height = 10
        self.active_label_index = 0
        self.values = values if len(values) > 0 else ["Empty"]
        self.is_active = False
        self.label_coordinates = []
        self.label_box_coordinates = []
        self.create_labels()
        self.value = lambda: self.values[self.active_label_index]
        self.arrow_image = load_image("menu/buttons/drop_down_arrow.png")

    def create_labels(self):
        font_size = 30
        font = pygame.font.Font(None, font_size)
        self.label_images = [font.render(label, True, (255, 255, 255)) for label in self.values]
        self.label_height = self.label_images[0].get_size()[1]

        option_x, option_y = self.x + 8, self.y
        for _ in self.label_images:
            option_y += self.label_height + 8
            box_coo = (option_x - 7, option_y)
            label_coo = (option_x, option_y + 5)
            self.label_box_coordinates.append(box_coo)
            self.label_coordinates.append(label_coo)

    def update_options(self, mouse_coo) -> bool:
        if not self.is_active:
            return False

        mouse_x, mouse_y = mouse_coo

        for index, (box_x, box_y) in enumerate(self.label_box_coordinates):
            if box_x <= mouse_x <= box_x + self.width and box_y <= mouse_y <= box_y + self.label_height:
                self.active_label_index = int(index)
                self.is_active = False
                return True
        return False

    def draw(self, screen: Surface):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (250, 250, 250), (self.x, self.y, self.width, self.height), 3)
        screen.blit(self.label_images[self.active_label_index], (self.x+8, self.y+8))
        screen.blit(self.arrow_image, (self.x + self.width-25, self.y+12))
        if self.is_active:
            for i, label in enumerate(self.label_images):
                box_coo = self.label_box_coordinates[i]
                if self.active_label_index == i:
                    pygame.draw.rect(screen, (0, 255, 255), (box_coo[0], box_coo[1], self.width, self.height))
                else:
                    pygame.draw.rect(screen, (100, 100, 100), (box_coo[0], box_coo[1], self.width, self.height))
                pygame.draw.rect(screen, (200, 200, 200), (box_coo[0], box_coo[1], self.width, self.height), 2)
                screen.blit(label, (self.label_coordinates[i][0], self.label_coordinates[i][1]))

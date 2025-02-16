from pygame import Surface
from src.pygapp.utils import graphics as grp
import pygame


class Button:
    pointer_image = grp.load_image("menu/info/pointer.png")

    def __init__(self, x: int, y: int, directory: str, effect):
        self.x = x
        self.y = y
        self.frame = 0
        if directory != "":
            self.image = grp.load_image(directory)
            self.size = self.image.get_size()
            self.rect = lambda: (self.x-self.frame*2,
                                 self.y-self.frame*2,
                                 self.size[0]+self.frame*4,
                                 self.size[1]+self.frame*4)
        self.effect = effect

    def cursor_is_inside(self, cursor_coo: (int, int)):
        cursor_x, cursor_y = cursor_coo[0], cursor_coo[1]
        button_width, button_height = self.image.get_size()[0], self.image.get_size()[1]
        return self.x <= cursor_x <= self.x + button_width and self.y <= cursor_y <= self.y + button_height

    def draw(self, screen: Surface, is_active=False):
        screen.blit(self.image, (self.x, self.y))

        if is_active:
            pygame.draw.rect(screen, (0, 255, 255), self.rect(), 2)  # rectangle to indicate which button is active
            self.frame = (self.frame+0.25) % 3  # current_frame = (last_frame + speed_of_effect) % (number of states-1)

    def draw_info(self, screen):
        screen.blit(self.pointer_image, (685, self.y + self.size[1] // 2 - 19))  # draw the head of the arrow (pointer)
        # line from pointer to center line (vertical)
        pygame.draw.line(screen, (0, 255, 255), (730, self.y + self.size[1] // 2 + 3), (730, 343), 5)
        # center line (horizontal)
        pygame.draw.rect(screen, (0, 255, 255), (728, 342, 30, 5))

    def change_image(self, directory: str):
        self.image = grp.load_image(directory)

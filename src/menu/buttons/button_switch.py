from ...pygapp.utils import audio
from src.menu.common.sounds import volume_change_sound
from .button import Button
from pygame import Surface
import pygame


class ButtonSwitch(Button):
    def __init__(self, x: int, y: int, directory: str, effect: str, id_c: int, behaviour: [callable], options):
        super().__init__(x, y, directory, effect)
        self.id = id_c
        self.options = options
        self.option_frame_length = 200//len(options)  # size dynamically created based on the size of the option's part
        self.options_x = [self.x+140+self.option_frame_length*i for i in range(len(options))]
        # behaviour 0 is a callable that gets the value of the switch according to the user configuration
        self.value = behaviour[0]()
        # active option is an integer representing the index of the option chosen in the index
        self.active_option = self.options.index(self.value)
        self.apply_change = behaviour[1]  # what the button does when one option is chosen
        
    def change_value(self, cursor: (int, int), add_value: int=None) -> None:
        if add_value is not None:
            self.active_option += add_value
        elif self.cursor_is_inside(cursor):  # cursor is the button
            for i, x in enumerate(self.options_x):
                if x <= cursor[0] <= x + 100 and self.y <= cursor[1] <= self.y + 50:
                    self.apply_change(i)
                    break
        else:
            self.active_option += 1

        self.active_option = min(max(self.active_option, 0), len(self.options))  # value never exceeds certain interval
        self.value = self.options[self.active_option]
        audio.play(volume_change_sound)

    def draw_info(self, screen):
        screen.blit(self.pointer_image, (710, self.y + self.size[1] // 2 - 19))  # draw the head of the arrow (pointer)
        # line from pointer to center line (vertical)
        pygame.draw.line(screen, (0, 255, 255), (755, self.y + self.size[1] // 2 + 3), (755, 343), 5)
        # center line (horizontal)
        pygame.draw.rect(screen, (0, 255, 255), (753, 342, 5, 5))

    def draw(self, screen: Surface, is_active=False):
        super().draw(screen)
        # draw the box around the chosen option
        # pygame.draw.rect(screen, (0, 255, 255), (self.options_x[self.active_option], self.y, 70, 35), 3)
        pygame.draw.rect(screen, (0, 0, 255),
                         (self.options_x[self.active_option], self.y+2, self.option_frame_length, 39),
                         3)
        """pygame.draw.rect(screen, (0, 0, 255), (self.options_x[self.active_option], self.y, 70, 35), 3)
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, 40, 40))
        pygame.draw.rect(screen, (0, 100, 255), (self.options_x[self.active_option]+3, self.y+3, 27, 32), 1)"""

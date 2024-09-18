import pygame
from pygame.event import Event
from src.menu.buttons import Button
from src.menu.sounds import button_y_sound
from src.pygapp.utils import audio


# provides a simple way of managing User input, both keyboard and mouse
class BasicInputManagement:
    EXIT_LINK = "exit"
    
    def __init__(self, buttons: [Button] = None):
        if buttons is None:
            buttons = []
        self.button_activation_sound = button_y_sound
        self.clock = pygame.time.Clock()
        self.button_list = buttons
        self.active_code = 0
        self.coord_effect = None
        self.already_checked_cursor = False  # True means that actions have already been taken regarding cursor position

    def set_button_to_active(self, new_active_code: int) -> None:
        if new_active_code == self.active_code:
            return
        
        audio.play(self.button_activation_sound)
        self.active_code = new_active_code
        self.coord_effect = self.update_coord_effect()

    def update_coord_effect(self) -> None:
        pass

    def manage_events(self) -> str:  # returns action to take based on input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return self.EXIT_LINK
            elif event.type == pygame.KEYDOWN:
                return self.get_effect_by_input(event)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.already_checked_cursor = True
                return self.get_effect_by_input()

    def manage_buttons(self, event: Event) -> str:
        if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
            return self.enter_action()

    def get_effect_by_input(self, event: Event = None) -> str:
        if event is not None:  # if the event is not None it means a key has been pressed
            return self.manage_buttons(event)
        # if it reaches this point, maybe there is some input given via mouse
        return self.manage_mouse()

    def cursor_is_on_button(self) -> bool:
        mouse_position = pygame.mouse.get_pos()
        for button_index, button in enumerate(self.button_list):
            if button.cursor_is_inside(mouse_position):
                self.set_button_to_active(button_index)
                return True
        return False

    def enter_action(self) -> str:
        return self.button_list[self.active_code].effect

    def manage_mouse(self) -> str:
        if self.cursor_is_on_button():
            return self.enter_action()
        self.already_checked_cursor = False  # allows the cursor to interact with buttons again after the User clicks

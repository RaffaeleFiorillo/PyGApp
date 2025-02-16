from .BaseWidget import BaseWidget
import pygame


class BaseContainer(BaseWidget):
    def __init__(self, x: int, y: int, width: int, height: int, widgets: [BaseWidget]):
        super().__init__(x, y, width, height)
        self.widgets = widgets

    def add_widget(self, widget: BaseWidget, position=(float, float), position_type="") -> None:
        """
        This method should be used anytime you want to add a widget to the container.
        :param widget: The widget to add to the Container
        :param position_type: The position of the widget will be set according to its type:
            ""   - The coordinates of the widget remain the same (In pixels and acting according to the pygame logic)
            "rp" - The value of the dimension is in pixels, and it is added to the Container corresponding dimension;
            "r%" - The value of the dimension is a percentage, and it determines the point where the center of the
                widget will be relative to the container. Ex: (0.5, 0.5) puts the widget in the container's center;
            Additional parameters can be added AT THE END of the parameter to the both types of relatives to indicate
             what part of the widget is the alignment point. "l"; "r"; "t"; "b" indicate left, right, top and bottom.
        :param position: Coordinates of the widget. Their interpretation depends on the position_type
        :return: None
        """
        pass

    def draw(self, screen: pygame.Surface):
        [widget.draw(screen) for widget in self.widgets]

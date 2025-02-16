from src.pygapp.utils import graphics as grp
from src.pygapp.widget.BaseWidget import BaseWidget


class BaseButton(BaseWidget):
    def __init__(self, x: int, y: int, width=0, height=0):
        super().__init__(x, y, width, height)
        self.is_active = False

    def cursor_is_inside(self, cursor_coo) -> bool:
        self.is_active = super().cursor_is_inside(cursor_coo)
        return self.is_active

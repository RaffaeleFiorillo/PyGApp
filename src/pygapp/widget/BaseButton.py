from .BaseWidget import BaseWidget


class BaseLinkButton(BaseWidget):
    def __init__(self, x: int, y: int, width: int, height: int, link: str):
        super().__init__(x, y, width, height)
        self.link = link
 
from src.template.CustomInterfaces.Menu.BaseMenu import BaseMenu


class NewMap(BaseMenu):
    link = "New"

    def __init__(self, screen):
        super().__init__(screen, "", None, None, None)

    @staticmethod
    def display(screen) -> str:
        mapp_maker_interface = NewMap(screen)
        next_link = mapp_maker_interface.start()
        return next_link

    def start(self) -> str:
        return "MainMenu"

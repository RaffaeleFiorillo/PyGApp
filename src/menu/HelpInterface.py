from src.template.CustomInterfaces.Menu.BaseMenu import BaseMenu


class Help(BaseMenu):
    link = "Help"

    def __init__(self, screen):
        super().__init__(screen, "", None, None, None)

    @staticmethod
    def display(screen) -> str:
        mapp_maker_interface = Help(screen)
        next_link = mapp_maker_interface.start()
        return next_link

    def start(self) -> str:
        return "MainMenu"

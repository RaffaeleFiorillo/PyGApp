from src.template.CustomInterfaces import BaseMenu
from src.template.CustomWidgets.MainMenuButton import MainMenuButton
from .ExitInterface import Exit
from .HelpInterface import Help
from .CreateAutomaticMapInterface import CreateAutomaticMap
from .SelectMap import SelectMap


class MainMenu(BaseMenu):
    link = "MainMenu"

    def __init__(self, screen, direct, buttons):
        super().__init__(screen, direct, buttons)

    @staticmethod
    def display(screen) -> str:
        # audio.stop_all_sounds()
        # audio.play(change_menu_sound)
        buttons = BaseMenu.create_buttons(MainMenuButton, "menu/buttons/1", [SelectMap.link, CreateAutomaticMap.link, Help.link, Exit.link])
        m_m = MainMenu(screen, f"menu/interfaces/Main/main menu.png", buttons)

        next_link = m_m.start()
        return next_link

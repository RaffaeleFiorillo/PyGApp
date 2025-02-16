from src.template.CustomInterfaces.Menu.SelectionMenu import SelectionMenu


class CreateAutomaticMap(SelectionMenu):
    link = "CreateAuto"

    def __init__(self, screen, buttons):
        super().__init__(screen, buttons)

    @staticmethod
    def display(screen) -> str:
        menu = CreateAutomaticMap.create_menu(screen, "assets/maps", file_extension="txt")
        next_link = menu.start()+"Auto"
        return next_link

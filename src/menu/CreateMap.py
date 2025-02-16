from src.template.CustomInterfaces.Menu.SelectionMenu import SelectionMenu


class CreateMap(SelectionMenu):
    link = "CreateMap"

    def __init__(self, screen, buttons):
        super().__init__(screen, buttons)

    @staticmethod
    def display(screen) -> str:
        menu = CreateMap.create_menu(screen, "assets/maps", file_extension="txt")
        next_link = menu.start()
        return next_link
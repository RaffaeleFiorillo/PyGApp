from src.template.CustomInterfaces import EditInterface


class EditMap(EditInterface):
    link = "Edit"

    def __init__(self, screen):
        super().__init__(screen)

    @staticmethod
    def display(screen) -> str:
        mapp_maker_interface = EditMap(screen)
        next_link = mapp_maker_interface.start()
        return next_link

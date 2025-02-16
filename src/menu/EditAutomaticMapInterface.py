from src.template.CustomInterfaces import GenerationInterface


class EditAutomaticMap(GenerationInterface):
    link = "EditAuto"

    def __init__(self, screen):
        super().__init__(screen)
        self.next_link_interface = "EditAuto"

    @staticmethod
    def display(screen) -> str:
        mapp_maker_interface = EditAutomaticMap(screen)
        next_link = mapp_maker_interface.start()
        return next_link
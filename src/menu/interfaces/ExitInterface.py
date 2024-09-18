from src.menu.bases.interface_bases import BaseInterface


class ExitInterface(BaseInterface):
	link = "exit"
	
	def __init__(self, screen):
		super().__init__(screen)
	
	@staticmethod
	def display_interface(screen):
		pass

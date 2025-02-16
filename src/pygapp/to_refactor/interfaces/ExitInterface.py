from src.pygapp.to_refactor.bases import BaseInterface


class ExitInterface(BaseInterface):
	link = "exit"
	
	def __init__(self, screen):
		super().__init__(screen)
	
	@staticmethod
	def display_interface(screen):
		pass

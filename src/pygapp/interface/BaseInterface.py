from pygame import Surface


class BaseInterface:
	"""
	This class provides a way to interact with the different functionalities of the software being built.
	"""
	
	# This is the link to this interface. No Interface can have the same link.
	link: str
	
	def __init__(self, screen: Surface, name=None):
		self.screen = screen  # screen surface where the Interface will be displayed
		self.name = self.link if name is not None else name  # the name of the menu (extracted from its directory)
	
	@staticmethod
	def display(screen: Surface) -> str:
		"""
		This method creates and starts an Interface instance.
		
		:param screen: The surface where the interface will be displayed (the *screen* property of the App instance)
		:return: The link for the interface that should be shown next
		"""
		raise Exception(f"Not implemented inherited method: *display_interface*")
	
	def start(self) -> str:
		"""
		Starts the interface process. This process ends when the link for the next interface is returned.
		
		:return: The link for the interface that should be shown next.
		"""
		raise Exception(f"Not implemented *start* method of Class: {self.__name__}")

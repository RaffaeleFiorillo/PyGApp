from pygame import Surface


class BaseWidget:
	def __init__(self, x: int, y: int, width: int, height: int, z: int = 0):
		"""
		Explicit initialization of the Widget.
		
		:param x: x coordentate on the screen
		:param y: y coordenate on the screen
		:param z: z coordentate on the screen (drawing priority)
		:param width: width of the widget
		:param height: height of the widget
		"""
		self.x = x
		self.y = y
		self.z = z
		self.width = width
		self.height = height
	
	def cursor_is_inside(self, cursor_coo: (int, int)):
		cursor_x, cursor_y = cursor_coo[0], cursor_coo[1]
		return self.x <= cursor_x <= self.x + self.width and self.y <= cursor_y <= self.y + self.height
	
	def draw(self, screen: Surface):
		raise Exception(f"Not implemented method *{self.__name__}.draw")

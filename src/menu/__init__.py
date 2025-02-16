from .ExitInterface import Exit
from .MainMenuInterface import MainMenu
from .NewMapInterface import NewMap
from .EditMapInterface import EditMap
from .CreateAutomaticMapInterface import CreateAutomaticMap
from .EditAutomaticMapInterface import EditAutomaticMap
from .HelpInterface import Help
from .SelectMap import SelectMap
from .CreateMap import CreateMap

STARTING_LINK = MainMenu.link  # the link to the interface chosen to be the starting point of the App
ENDING_LINK = Exit.link
INTERFACE_LIST = [MainMenu, Exit, SelectMap, CreateMap, EditMap, CreateAutomaticMap, EditAutomaticMap]

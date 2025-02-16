import pygame
from src.app_config import SCREEN, SCREEN_LABEL, SCREEN_ICON_IMAGE_PATH
from src.menu import INTERFACE_LIST, STARTING_LINK, ENDING_LINK
from src.pygapp.utils import graphics as grp


class App:
    """
        Generic App class that encapsulates the logic for switching between the apps menu. \n
        It uses the MENU_LINKS to establish this interface switching behavior. \n
        Basically this class just creates the connection between the different menu created in the "menu" package.
    """
    # This variable holds a dictionary with the structure: {(str)*InterfaceLink*: (callable)*InterfaceDisplayFunction*}
    # The *InterfaceLink* is a unique identification for the interface;
    # The *InterfaceDisplayFunction* is a function that displays an interface and returns the link to the next interface
    interfaces: {str: callable} = {}
    # The screen is the main surface of the App (where all the images will be shown)
    screen: pygame.Surface = SCREEN

    def __init__(self):
        app_label = SCREEN_LABEL if SCREEN_LABEL else "PyGApp Application"
        pygame.display.set_caption(app_label)
        icon_image_path = SCREEN_ICON_IMAGE_PATH if SCREEN_ICON_IMAGE_PATH else "icon.ico"
        pygame.display.set_icon(grp.load_image(icon_image_path))
        
        self._create_interfaces_links()

    def _create_interfaces_links(self):
        """
            Creates the *interface* property in a way that the App can use it to navigate throgh the menu.\n
            The App will include an Interface only if it is inside the src.menu.INTERFACE_LIST variable. \n
            :raises Exception: If a duplicated link is found (two Interfaces have the same link value).
        """
        
        for interface in INTERFACE_LIST:
            if interface.link in self.interfaces:
                raise Exception(f"Duplicated interface link found: {interface.__name__}.{interface.link}")
            self.interfaces[interface.link] = interface.display
    
    def start(self) -> None:
        current_link = STARTING_LINK
        keep_app_running = True
        
        while keep_app_running:
            previous_link = current_link  # saving current link in case there is the need to go back
            current_interface_display_function = self.interfaces[current_link]
            # Starting the interface cycle. Once the cycle finishes, the link to the next interface is returned.
            next_interface_link = current_interface_display_function(self.screen)

            # If the user clicks the closing button (top right red crux) the next link returned is either a False value
            # (or equivalent) or directly the  ENDING_LINK
            if not next_interface_link or next_interface_link == ENDING_LINK:
                # the EndingInterface returns either True or False based on the User's choice to exit the App
                # this value is then used to update the keep_app_running variable
                keep_app_running = self.interfaces[ENDING_LINK](self.screen)
                # In case the user wants to keep using the app, it goes back to the interface he was in before clicking
                # the closing button.
                current_link = previous_link
            else:
                current_link = next_interface_link

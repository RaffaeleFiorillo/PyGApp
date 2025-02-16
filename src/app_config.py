import pygame

pygame.init()  # Initiate pygame to ensure all its components work

# -------------------------------------------------- SCREEN ------------------------------------------------------------
SCREEN_WIDTH = 1080   # width of the App's window
SCREEN_HEIGHT = 680  # height of the App's window
SCREEN_LABEL = "MApPy - Beta"  # Label shown in the App's window. If left empty, the default label will be used
SCREEN_ICON_IMAGE_PATH = ""  # path to the icon image for the App. If left empty, the default icon will be used
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

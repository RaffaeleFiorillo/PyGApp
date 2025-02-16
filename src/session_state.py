from src.template.CustomWidgets.MapProject import MapProject
from src.template.CustomWidgets.MapWidget import Map

class SessionState:
    template_name = "Initial Template"
    map_directory = ""
    data = {}
    map: Map = None
    project: MapProject = None

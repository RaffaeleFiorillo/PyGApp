from files import create_folder


def create_app_structure(directory: str) -> None:
	"""
		Creates the complete structure for an Application that will use the PyGApp framework.
		
		:parameter directory: The directory where the Application structure will be created. A full path must be provided.
	"""
	# Step 1: Create all the assets folders
	create_folder("assets", directory)
	create_folder("audio", f"{directory}/assets")
	create_folder("data", f"{directory}/assets")
	create_folder("images", f"{directory}/assets")
	
	# Step 2: Create the src structure
	create_folder("src", directory)
	
	# Step 2: Create all the files
	
	pass
	
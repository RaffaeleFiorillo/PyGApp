import os
import shutil
from .encryption import decrypt_file, encrypt_file


def create_path_string(element_path: str, path_is_absolute) -> str:
    return element_path if path_is_absolute else os.path.join("assets", element_path)


def create_folder(folder_name: str, directory: str, path_is_absolute=False) -> None:
    """
    Creates a folder in a specific directory (including any intermediate directories).

    :param folder_name: The name of the folder to be created.
    :param directory: The directory where the folder will be created.
    :param path_is_absolute: If True, the directory's path starts from the directory of the python file being executed.
                             If False: The starting point of the directory's path is the assets' folder.
    """
    folder_path = create_path_string(os.path.join(directory, folder_name), path_is_absolute)

    # If the folder does not already exist, create it (including any intermediate directories)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def delete_folder(folder_path: str, path_is_absolute=False, force_delete=False) -> None:
    """
    Deletes a folder in a specific directory. Optionally also deletes all files inside the folder.

    :param folder_path: The path to the folder to be deleted.
    :param path_is_absolute: If True, the directory's path starts from the directory of the Python file being executed.
                             If False, the starting point of the directory's path is the assets' folder.
    :param force_delete: When True, all files inside the folder will be deleted before deleting the folder.
    """
    # Determine the folder path based on whether the path is absolute or relative to the assets folder
    folder_path = create_path_string(folder_path, path_is_absolute)

    # If the folder does not exist there is no need to delete it
    if not os.path.exists(folder_path):
        return

    # If force_delete is True, delete all files inside the folder first
    if force_delete:
        delete_folder_content(folder_path, path_is_absolute=True)

    # Attempt to delete the folder
    try:
        shutil.rmtree(folder_path)
    except OSError as e:
        # currently passing, but should use log system to save the errors in a separate txt file
        # f"Failed to delete the folder '{folder_path}': {e.strerror}"
        pass


def delete_folder_content(folder_path: str, path_is_absolute=False) -> None:
    """
    Deletes all the files in a given folder.

    :param folder_path: The path to the folder to be deleted.
    :param path_is_absolute: If True, the directory's path starts from the directory of the Python file being executed.
                             If False, the starting point of the directory's path is the assets' folder.
    """
    # Determine the folder path based on whether the path is absolute or relative to the assets folder
    folder_path = create_path_string(folder_path, path_is_absolute)
    
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for direc in dirs:
                shutil.rmtree(os.path.join(root, direc))
    except OSError as e:
        # currently passing, but should use log system to save the errors in a separate txt file
        # f"Failed to delete contents of the folder '{folder_path}': {e.strerror}"
        pass


def read_file_content(file_path: str, path_is_absolute=False, lines_to_read=0, file_is_encrypted=False) -> [str]:
    """
    Reads the content of a given file.
    
    :param file_path: Full path to the file.
    :param path_is_absolute: If True, the directory's path starts from the directory of the Python file being executed.
                             If False, the starting point of the directory's path is the assets' folder.
    :param lines_to_read: The number of lines to read from the file. By default, (zero), all the lines are read.
    :param file_is_encrypted: The file being read is encrypted, and you want the content to be decrypted.
    :return: A list with all the lines inside the file.
    """
    file_path = create_path_string(file_path, path_is_absolute)
    
    if file_is_encrypted:
        decrypt_file(file_path)
        
    with open(file_path, "r") as file:
        file_content = file.readlines() if lines_to_read == 0 else [file.readline() for _ in range(lines_to_read)]
        
    if file_is_encrypted:
        encrypt_file(file_path)
        
    return file_content


def write_file_content(content: [str], file_path: str, path_is_absolute=False) -> None:
    """
    Writes lines of text inside a given file.
    
    :param content: A list of strings. Every element of the list is a new line to write in the file.
    :param file_path: Full path to the file.
    :param path_is_absolute: If True, the directory's path starts from the directory of the Python file being executed.
                             If False, the starting point of the directory's path is the assets' folder.
    """
    file_path = create_path_string(file_path, path_is_absolute)
    with open(file_path, "w") as file:
        file.writelines(content)
    encrypt_file(file_path)


def erase_file_data(file_path: str, path_is_absolute=False) -> None:
    """
    Erases the content of a given file.
    
    :param file_path: Full path to the file.
    :param path_is_absolute: If True, the directory's path starts from the directory of the Python file being executed.
                             If False, the starting point of the directory's path is the assets' folder.
    """
    file_path = file_path if path_is_absolute else os.path.join("assets", file_path)
    with open(file_path, "w"):
        pass

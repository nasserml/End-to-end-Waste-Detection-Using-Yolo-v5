import os.path
import sys
import yaml
import base64

from wasteDetection.exception import AppException
from wasteDetection.logger import logging

"""
    Reads a YAML file and returns its contents as a dictionary.

    Parameters:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The contents of the YAML file as a dictionary.

    Raises:
        AppException: If an error occurs while reading the YAML file.
"""

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise AppException(e, sys) from e
    



"""
    Writes the given content as YAML to the specified file path.

    Parameters:
        file_path (str): The path of the file to write the YAML content to.
        content (object): The content to write as YAML.
        replace (bool, optional): If set to True, replaces the file if it already exists. Defaults to False.

    Returns:
        None
"""
    
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write_yaml_file")

    except Exception as e:
        raise AppException(e, sys)
    

    """
    Decodes an image from a base64 string and saves it to a file.

    Parameters:
        imgstring (str): The base64 encoded image string to decode.
        fileName (str): The name of the file to save the decoded image.

    Returns:
        None
    """

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

    """
    Encodes an image file into base64 format.

    Args:
        croppedImagePath (str): The path to the cropped image file.

    Returns:
        bytes: The image file encoded in base64 format.
    """
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

    
    
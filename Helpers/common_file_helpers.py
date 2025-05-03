import json
import os

from Utilities import common_utils


def move_file(file_path, new_file_path):
    """Move a file to a new location."""
    log = common_utils.custom_logger()
    if os.path.exists(file_path):
        os.rename(file_path, new_file_path)
        log.info(f"File moved from {file_path} to {new_file_path}")
        return True
    log.error(f"File not found: {file_path}")
    return False


def rename_file(file_path, new_file_name):
    """Rename a file."""
    log = common_utils.custom_logger()
    if os.path.exists(file_path):
        directory = os.path.dirname(file_path)
        new_file_path = os.path.join(directory, new_file_name)
        os.rename(file_path, new_file_path)
        log.info(f"File renamed from {file_path} to {new_file_path}")
        return True
    log.error(f"File not found: {file_path}")
    return False


def get_file_name(file_path):
    """Get the name of a file without the extension."""
    log = common_utils.custom_logger()
    if os.path.exists(file_path):
        file = os.path.basename(file_path)
        file_name = os.path.splitext(file)[0]
        log.info(f"File name: {file_name}")
        return file_name
    log.error(f"File not found: {file_path}")
    return None


def get_absolute_file_path(relative_file_path):
    """Get the full path of a file."""
    log = common_utils.custom_logger()
    if os.path.exists(relative_file_path):
        full_path = os.path.abspath(relative_file_path)
        log.info(f"Full path: {full_path}")
        return full_path
    log.error(f"File not found: {relative_file_path}")
    return None


def delete_file(file_path):
    """Delete a file."""
    log = common_utils.custom_logger()
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            log.info(f"File deleted: {file_path}")
            return True
        return False
    except PermissionError:
        print(f"Permission denied: {file_path}")
        log.error(f"Permission denied: {file_path}")
        return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        log.error(f"Error deleting file: {e}")
        return False


def load_data_from_json(json_file):
    """Load data from a JSON file."""
    log = common_utils.custom_logger()
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            log.info(f"Data loaded from JSON: {data}")
            return data
    except FileNotFoundError:
        print("File not found: data.json")
        log.error("File not found: data.json")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        log.error(f"Error decoding JSON: {e}")
        return None
    except Exception as e:
        print(f"Error loading data from JSON: {e}")
        log.error(f"Error loading data from JSON: {e}")
        return None

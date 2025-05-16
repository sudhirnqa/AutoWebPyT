import json
import os

from Utilities import common_utils


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


def load_data_from_json(json_file):
    """Load data from a JSON file."""
    log = common_utils.custom_logger()
    try:
        with open(json_file, "r", encoding="utf-8") as file:
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

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

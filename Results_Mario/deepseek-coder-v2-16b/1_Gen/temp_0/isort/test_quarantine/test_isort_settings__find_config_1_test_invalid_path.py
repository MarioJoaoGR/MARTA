
import os
from typing import Any
from isort.settings import MAX_CONFIG_SEARCH_DEPTH, CONFIG_SOURCES, CONFIG_SECTIONS, STOP_CONFIG_SEARCH_ON_DIRS
from warnings import warn

def _find_config(path: str) -> tuple[str, dict[str, Any]]:
    """
    Searches for configuration files in the given directory and its subdirectories up to a predefined depth. It supports TOML and INI (editorconfig) formats. The function attempts to read configuration data from each found file based on specified sections. If no configuration file is found or an error occurs during reading, it returns the initial path with empty configuration data.
    
    Parameters:
        path (str): The directory path where the search for configuration files begins. This can be either a relative or absolute path to a directory.
        
    Returns:
        tuple[str, dict[str, Any]]: A tuple containing the last searched directory and a dictionary of configuration data found in the configuration file(s). If no configuration file is found, it returns the initial path with an empty dictionary.
    
    Examples:
        To find configuration files starting from the current working directory:
            config_data = _find_config(".")
        
        To find configuration files starting from a specific directory:
            config_data = _find_config("/path/to/directory")
    
    Notes:
        - The function searches for configuration files in the specified directory and its subdirectories up to MAX_CONFIG_SEARCH_DEPTH levels deep.
        - It supports TOML and INI (editorconfig) formats, automatically detecting the format based on the file extension.
        - Configuration data is retrieved from each found file based on the section names provided in CONFIG_SECTIONS. If a configuration file cannot be read or does not contain any relevant sections, it will return an empty dictionary for that file.
        - The function logs warnings if it fails to retrieve configuration information from a specific file.
    """
    current_directory = path
    tries = 0
    while current_directory and tries < MAX_CONFIG_SEARCH_DEPTH:
        for config_file_name in CONFIG_SOURCES:
            potential_config_file = os.path.join(current_directory, config_file_name)
            if os.path.isfile(potential_config_file):
                config_data: dict[str, Any] = {}  # Initialize the dictionary here
                try:
                    config_data = _get_config_data(
                        potential_config_file, CONFIG_SECTIONS[config_file_name]
                    )
                except Exception:
                    warn(
                        f"Failed to pull configuration information from {potential_config_file}",
                        stacklevel=2,
                    )
                if config_data:
                    return (current_directory, config_data)

        for stop_dir in STOP_CONFIG_SEARCH_ON_DIRS:
            if os.path.isdir(os.path.join(current_directory, stop_dir)):
                return (current_directory, {})

        new_directory = os.path.split(current_directory)[0]
        if new_directory == current_directory:
            break

        current_directory = new_directory
        tries += 1

    return (path, {})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__find_config_1_test_invalid_path
isort/Test4DT_tests/test_isort_settings__find_config_1_test_invalid_path.py:38:34: E0602: Undefined variable '_get_config_data' (undefined-variable)


"""
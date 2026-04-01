
import os
from typing import Any, Dict
from isort.settings import CONFIG_SOURCES, CONFIG_SECTIONS, Trie
from warnings import warn

def find_all_configs(path: str) -> Trie:
    """
    Finds all configuration files in a given directory and its subdirectories.

    Parameters:
        path (str): The directory to search for configuration files.

    Returns:
        Trie | None: A trie data structure representing the configurations found, or None if no configurations are found.

    Usage:
        To find all configuration files in a specific directory, you can call this function with the desired path as an argument. For example:
        ```python
        config_trie = find_all_configs("path/to/config/directory")
        ```
        This will search for configuration files (e.g., `.isort.cfg`, `pyproject.toml` with a [tool.isort] section) in the specified directory and its subdirectories, building a trie structure to represent these configurations. If no configurations are found, it returns None.
    """
    trie_root = Trie("default", {})

    for dirpath, _, _ in os.walk(path):
        for config_file_name in CONFIG_SOURCES:
            potential_config_file = os.path.join(dirpath, config_file_name)
            if os.path.isfile(potential_config_file):
                config_data: Dict[str, Any]
                try:
                    config_data = _get_config_data(
                        potential_config_file, CONFIG_SECTIONS[config_file_name]
                    )
                except Exception:
                    warn(
                        f"Failed to pull configuration information from {potential_config_file}",
                        stacklevel=2,
                    )
                    config_data = {}

                if config_data:
                    trie_root.insert(potential_config_file, config_data)
                    break

    return trie_root

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_find_all_configs_0_test_invalid_directory
isort/Test4DT_tests/test_isort_settings_find_all_configs_0_test_invalid_directory.py:32:34: E0602: Undefined variable '_get_config_data' (undefined-variable)


"""
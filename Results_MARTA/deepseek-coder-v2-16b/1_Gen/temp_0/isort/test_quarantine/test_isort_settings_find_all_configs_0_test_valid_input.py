
import pytest
from isort.settings import CONFIG_SOURCES, CONFIG_SECTIONS
from isort.trie import Trie
from isort.utils import _get_config_data
from warnings import warn
import os

def find_all_configs(path: str) -> Trie:
    """
    Looks for config files in the path provided and in all of its sub-directories.
    Parses and stores any config file encountered in a trie and returns the root of
    the trie
    """
    trie_root = Trie("default", {})

    for dirpath, _, _ in os.walk(path):
        for config_file_name in CONFIG_SOURCES:
            potential_config_file = os.path.join(dirpath, config_file_name)
            if os.path.isfile(potential_config_file):
                config_data: dict[str, Any]
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
************* Module Test4DT_tests.test_isort_settings_find_all_configs_0_test_valid_input
isort/Test4DT_tests/test_isort_settings_find_all_configs_0_test_valid_input.py:4:0: E0401: Unable to import 'isort.trie' (import-error)
isort/Test4DT_tests/test_isort_settings_find_all_configs_0_test_valid_input.py:4:0: E0611: No name 'trie' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_settings_find_all_configs_0_test_valid_input.py:5:0: E0611: No name '_get_config_data' in module 'isort.utils' (no-name-in-module)
isort/Test4DT_tests/test_isort_settings_find_all_configs_0_test_valid_input.py:21:39: E0602: Undefined variable 'Any' (undefined-variable)


"""
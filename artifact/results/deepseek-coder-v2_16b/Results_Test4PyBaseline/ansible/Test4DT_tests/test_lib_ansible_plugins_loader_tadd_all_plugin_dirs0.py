# Module: ansible.plugins.loader
import os
from ansible.plugins.loader import add_all_plugin_dirs

def test_add_all_plugin_dirs_valid_directory():
    # Assuming the function works correctly and adds directories if they exist
    pass  # Add assertions here to validate the behavior for a valid directory

def test_add_all_plugin_dirs_invalid_path():
    # Assuming the function displays a warning message for invalid paths
    pass  # Add assertions here to validate the warning message and no action taken for an invalid path

def test_add_all_plugin_dirs_relative_path():
    # Assuming the function handles relative paths correctly
    pass  # Add assertions here to validate the behavior for a relative path

def test_add_all_plugin_dirs_home_directory():
    # Assuming the function expands home directory paths correctly
    pass  # Add assertions here to validate the behavior for a home directory path

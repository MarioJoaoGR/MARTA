
import os
from ansible.plugins.loader import add_all_plugin_dirs

def test_add_all_plugin_dirs_valid_directory():
    temp_dir = "temp_test_dir"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    add_all_plugin_dirs(temp_dir)  # Call the function with a valid directory
    
    assert os.path.isdir(os.path.expanduser(temp_dir)), "The provided path should be recognized as a directory"
    os.rmdir(temp_dir)  # Clean up after the test

def test_add_all_plugin_dirs_invalid_path():
    invalid_path = "nonexistent_directory"
    add_all_plugin_dirs(invalid_path)  # Call the function with an invalid path
    
    assert not os.path.exists(os.path.expanduser(invalid_path)), f"The provided path '{invalid_path}' should not exist"

def test_add_all_plugin_dirs_relative_path():
    relative_path = "relative/path"
    add_all_plugin_dirs(relative_path)  # Call the function with a relative path
    
    assert not os.path.isabs(os.path.expanduser(relative_path)), "The provided relative path should not be converted to an absolute path"

def test_add_all_plugin_dirs_home_directory():
    home_dir = os.path.expanduser("~")  # Get the user's home directory
    add_all_plugin_dirs(home_dir)  # Call the function with the home directory
    
    assert os.path.isdir(os.path.expanduser(home_dir)), "The provided path should be recognized as a directory"

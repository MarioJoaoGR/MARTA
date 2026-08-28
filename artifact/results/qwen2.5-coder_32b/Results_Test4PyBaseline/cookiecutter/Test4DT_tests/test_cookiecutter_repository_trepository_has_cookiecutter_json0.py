# Module: cookiecutter.repository
import os
from cookiecutter.repository import repository_has_cookiecutter_json
import tempfile
import shutil

def test_repository_has_cookiecutter_json_with_valid_repo():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a valid repository directory with 'cookiecutter.json'
        json_path = os.path.join(temp_dir, 'cookiecutter.json')
        with open(json_path, 'w') as f:
            f.write('{}')
        
        assert repository_has_cookiecutter_json(temp_dir) is True

def test_repository_has_cookiecutter_json_with_invalid_repo():
    # Test with a non-existent directory
    assert repository_has_cookiecutter_json('/path/to/nonexistent_directory') is False

def test_repository_has_cookiecutter_json_without_cookiecutter_json():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create an empty directory without 'cookiecutter.json'
        assert repository_has_cookiecutter_json(temp_dir) is False

def test_repository_has_cookiecutter_json_with_empty_string():
    # Test with an empty string as the directory path
    assert repository_has_cookiecutter_json('') is False

def test_repository_has_cookiecutter_json_with_file_instead_of_directory():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        try:
            # Test with a file path instead of a directory path
            assert repository_has_cookiecutter_json(temp_file.name) is False
        finally:
            os.remove(temp_file.name)

def test_repository_has_cookiecutter_json_with_special_characters():
    with tempfile.TemporaryDirectory() as temp_dir:
        special_chars_dir = os.path.join(temp_dir, 'special@#chars$%^&*()')
        os.makedirs(special_chars_dir)
        
        # Create a valid repository directory with 'cookiecutter.json'
        json_path = os.path.join(special_chars_dir, 'cookiecutter.json')
        with open(json_path, 'w') as f:
            f.write('{}')
        
        assert repository_has_cookiecutter_json(special_chars_dir) is True

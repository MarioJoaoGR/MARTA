
import os
import json
import tempfile
import shutil
import pytest
from cookiecutter.replay import load

# Define a temporary directory for testing
TEST_DIR = None

def setup_module(module):
    """Setup module by creating the test directory and game_data.json file."""
    global TEST_DIR
    TEST_DIR = tempfile.mkdtemp()
    with open(os.path.join(TEST_DIR, 'game_data.json'), 'w') as f:
        json.dump({'cookiecutter': {'name': 'example', 'version': '1.0'}}, f)

def teardown_module(module):
    """Teardown module by removing the test directory."""
    global TEST_DIR
    if TEST_DIR and os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)

def get_file_name(replay_dir, template_name):
    """Helper function to construct the file name with .json extension if needed."""
    if not template_name.endswith('.json'):
        template_name += '.json'
    return os.path.join(replay_dir, template_name)

@pytest.fixture
def valid_replay_data():
    """Fixture to provide a valid replay data dictionary."""
    return {'cookiecutter': {'name': 'example', 'version': '1.0'}}

def test_valid_case(valid_replay_data):
    """Test loading a valid case with correct parameters."""
    result = load(TEST_DIR, 'game_data')
    assert result == valid_replay_data

def test_valid_case_with_json_extension(valid_replay_data):
    """Test loading a valid case with the .json extension included in the template name."""
    result = load(TEST_DIR, 'game_data.json')
    assert result == valid_replay_data

def test_invalid_template_name_type():
    """Test that an invalid type for template_name raises a TypeError."""
    with pytest.raises(TypeError):
        load(TEST_DIR, 123)

def test_missing_cookiecutter_key():
    """Test that a missing 'cookiecutter' key in the JSON file raises a ValueError."""
    with open(os.path.join(TEST_DIR, 'invalid_data.json'), 'w') as f:
        json.dump({'name': 'example', 'version': '1.0'}, f)
    with pytest.raises(ValueError):
        load(TEST_DIR, 'invalid_data')

def test_empty_template_name():
    """Test that an empty string for template_name raises a FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        load(TEST_DIR, '')

def test_none_replay_dir():
    """Test that None as replay_dir raises a TypeError."""
    with pytest.raises(TypeError):
        load(None, 'game_data')

def test_nonexistent_file():
    """Test that a non-existent file raises a FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        load(TEST_DIR, 'non_existent')

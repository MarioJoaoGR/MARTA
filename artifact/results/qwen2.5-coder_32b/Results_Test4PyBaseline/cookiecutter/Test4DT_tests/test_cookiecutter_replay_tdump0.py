
import os
import pytest
import json  # Importing the json module to handle JSON file operations
from cookiecutter.replay import dump

def setup_module(module):
    """Setup a temporary directory for the tests."""
    module.temp_dir = '/tmp/test_cookiecutter_replay'
    if not os.path.exists(module.temp_dir):
        os.makedirs(module.temp_dir)

def teardown_module(module):
    """Cleanup the temporary directory after tests."""
    if os.path.exists(module.temp_dir):
        for filename in os.listdir(module.temp_dir):
            file_path = os.path.join(module.temp_dir, filename)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
        os.rmdir(module.temp_dir)

def test_dump_creates_directory(tmp_path):
    """Test that the function creates the directory if it does not exist."""
    non_existent_dir = tmp_path / 'nonexistent'
    assert not os.path.exists(non_existent_dir)
    dump(str(non_existent_dir), 'test_template', {'cookiecutter': {}})
    assert os.path.exists(non_existent_dir)

def test_dump_writes_json_file(tmp_path):
    """Test that the function writes a JSON file with the correct content."""
    template_name = 'test_template'
    context_data = {'cookiecutter': {'project_name': 'example'}}
    dump(str(tmp_path), template_name, context_data)
    replay_file = tmp_path / f'{template_name}.json'
    assert os.path.exists(replay_file)
    with open(replay_file, 'r') as infile:
        content = json.load(infile)
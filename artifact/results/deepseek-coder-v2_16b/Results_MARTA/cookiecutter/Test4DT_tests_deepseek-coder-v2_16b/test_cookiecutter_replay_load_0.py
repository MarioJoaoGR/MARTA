
import pytest
from cookiecutter.replay import load
import json

def get_file_name(replay_dir, template_name):
    if not template_name.endswith('.json'):
        template_name += '.json'
    return f"{replay_dir}/{template_name}"

# Test for valid input scenario

# Test for empty string template name scenario

# Test for file not found scenario
def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load('data', 'nonexistent')
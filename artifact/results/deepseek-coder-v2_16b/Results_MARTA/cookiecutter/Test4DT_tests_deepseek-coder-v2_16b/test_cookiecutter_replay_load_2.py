
import pytest
from cookiecutter.replay import load
import os
import json

def get_file_name(replay_dir, template_name):
    if not template_name.endswith('.json'):
        template_name += '.json'
    return os.path.join(replay_dir, template_name)



def test_invalid_directory():
    with pytest.raises(FileNotFoundError):
        load('nonexistent_dir', 'example')

import pytest
from cookiecutter.replay import load
import os
import json

def get_file_name(replay_dir, template_name):
    if not template_name.endswith('.json'):
        template_name += '.json'
    return os.path.join(replay_dir, template_name)



def test_invalid_template_type():
    replay_dir = 'data'
    template_name = 12345  # Invalid type (int)
    with pytest.raises(TypeError):
        load(replay_dir, template_name)
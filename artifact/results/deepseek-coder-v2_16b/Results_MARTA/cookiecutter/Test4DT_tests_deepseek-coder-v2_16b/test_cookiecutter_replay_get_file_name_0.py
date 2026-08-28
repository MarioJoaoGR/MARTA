
import pytest
import os
from cookiecutter.replay import get_file_name



def test_valid_input_with_json_suffix():
    replay_dir = 'data'
    template_name = 'example'
    expected_output = os.path.join(replay_dir, 'example.json')
    assert get_file_name(replay_dir, template_name) == expected_output

def test_valid_input_with_existing_json_suffix():
    replay_dir = 'data'
    template_name = 'example.json'
    expected_output = os.path.join(replay_dir, 'example.json')
    assert get_file_name(replay_dir, template_name) == expected_output
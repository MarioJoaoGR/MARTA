
import os
from unittest.mock import patch, MagicMock
import pytest
from cookiecutter.replay import get_file_name

# Test for valid case where both replay_dir and template_name are provided
def test_valid_case():
    replay_dir = 'data'
    template_name = 'example'
    expected_output = os.path.join(replay_dir, 'example.json')
    assert get_file_name(replay_dir, template_name) == expected_output

# Test for case where template_name already ends with '.json'
def test_template_name_ends_with_json():
    replay_dir = 'logs'
    template_name = 'logfile.json'
    expected_output = os.path.join(replay_dir, 'logfile.json')
    assert get_file_name(replay_dir, template_name) == expected_output

# Test for edge case where replay_dir is None
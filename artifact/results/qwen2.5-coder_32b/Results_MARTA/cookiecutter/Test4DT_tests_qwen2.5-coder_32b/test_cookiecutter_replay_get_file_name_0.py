
import os
from cookiecutter.replay import get_file_name

def test_valid_input_no_extension():
    replay_dir = '/path/to/replays'
    template_name = 'game_data'
    expected_output = '/path/to/replays/game_data.json'
    assert get_file_name(replay_dir, template_name) == expected_output

def test_valid_input_with_extension():
    replay_dir = '/path/to/replays'
    template_name = 'game_data.json'
    expected_output = '/path/to/replays/game_data.json'
    assert get_file_name(replay_dir, template_name) == expected_output

def test_invalid_input_empty_strings():
    replay_dir = ''
    template_name = ''
    expected_output = '.json'  # Assuming the function should return just '.json' if both inputs are empty
    assert get_file_name(replay_dir, template_name) == expected_output

def test_valid_input_different_directory():
    replay_dir = '/another/directory'
    template_name = 'session_123'
    expected_output = '/another/directory/session_123.json'
    assert get_file_name(replay_dir, template_name) == expected_output

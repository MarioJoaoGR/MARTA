# Module: cookiecutter.replay
import os
from cookiecutter.replay import get_file_name

def test_get_file_name_without_json_extension():
    assert get_file_name('/path/to/directory', 'data') == '/path/to/directory/data.json'
    assert get_file_name('relative/path', 'config') == 'relative/path/config.json'

def test_get_file_name_with_json_extension():
    assert get_file_name('/another/path', 'config.json') == '/another/path/config.json'
    assert get_file_name('replays', 'user_settings.json') == 'replays/user_settings.json'

def test_get_file_name_empty_replay_dir():
    assert get_file_name('', 'data') == 'data.json'
    assert get_file_name('', 'file_with_extension.json') == 'file_with_extension.json'

def test_get_file_name_trailing_slash_in_replay_dir():
    assert get_file_name('/path/to/directory/', 'data') == '/path/to/directory/data.json'
    assert get_file_name('relative/path/', 'config.json') == 'relative/path/config.json'

def test_get_file_name_with_special_characters():
    assert get_file_name('/special/chars', 'file@name#with$special%chars') == '/special/chars/file@name#with$special%chars.json'
    assert get_file_name('another/special', 'file&name*with^more(special)chars.json') == 'another/special/file&name*with^more(special)chars.json'

def test_get_file_name_with_numeric_names():
    assert get_file_name('/numeric/names', '12345') == '/numeric/names/12345.json'
    assert get_file_name('numbers', '67890.json') == 'numbers/67890.json'

def test_get_file_name_with_whitespace():
    assert get_file_name('/path/to/directory', 'file name with spaces') == '/path/to/directory/file name with spaces.json'
    assert get_file_name('spaces in path', 'filename  .json') == 'spaces in path/filename  .json'

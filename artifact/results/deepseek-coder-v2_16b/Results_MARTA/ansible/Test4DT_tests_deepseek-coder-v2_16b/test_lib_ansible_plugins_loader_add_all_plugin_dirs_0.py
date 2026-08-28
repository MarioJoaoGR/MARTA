
import os
from unittest.mock import patch
import pytest
from ansible.plugins.loader import PluginPathContext

def add_all_plugin_dirs(path):
    ''' Add any existing plugin dirs in the path provided, expanding user home directory if necessary. It checks each potential plugin subdirectory for validity and adds it as a plugin directory if found. If the provided path is not a directory, it warns about the invalid path. '''
    b_path = os.path.expanduser(to_bytes(path, errors='surrogate_or_strict'))
    if os.path.isdir(b_path):
        for name, obj in get_all_plugin_loaders():
            if obj.subdir:
                plugin_path = os.path.join(b_path, to_bytes(obj.subdir))
                if os.path.isdir(plugin_path):
                    obj.add_directory(to_text(plugin_path))
    else:
        display.warning("Ignoring invalid path provided to plugin path: '%s' is not a directory" % to_text(path))

@pytest.fixture
def valid_dir():
    yield '/valid/path/to/plugins'

@pytest.fixture
def invalid_dir():
    yield 'invalid-path'

@pytest.fixture
def none_input():
    yield None

def test_valid_input(valid_dir):
    with patch('os.path.isdir', return_value=True):
        add_all_plugin_dirs(valid_dir)
        assert PluginPathContext._paths == [valid_dir]

def test_invalid_input(invalid_dir):
    with patch('os.path.isdir', return_value=False):
        with pytest.warns(UserWarning, match="Ignoring invalid path provided to plugin path: 'invalid-path' is not a directory"):
            add_all_plugin_dirs(invalid_dir)

def test_none_input(none_input):
    with patch('os.path.isdir', return_value=False):
        with pytest.warns(UserWarning, match="Ignoring invalid path provided to plugin path: 'None' is not a directory"):
            add_all_plugin_dirs(none_input)

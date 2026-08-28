
import os
import pytest
from ansible.module_utils.facts.system.distribution import _file_exists


def test_invalid_file():
    # Test an invalid path (non-existent file)
    assert _file_exists('nonexistentfile.txt') == False


def test_invalid_path():
    # Test an invalid path (non-existent file), even if allow_empty is set to True
    with pytest.raises(Exception):
        assert _file_exists('nonexistentfile.txt', allow_empty=True)
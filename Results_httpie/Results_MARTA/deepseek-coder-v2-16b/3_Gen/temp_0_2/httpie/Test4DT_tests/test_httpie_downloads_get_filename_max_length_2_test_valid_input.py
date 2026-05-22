
import pytest
from unittest.mock import patch, MagicMock
import os

def get_filename_max_length(directory: str) -> int:
    max_len = 255
    if hasattr(os, 'pathconf') and 'PC_NAME_MAX' in os.pathconf_names:
        max_len = os.pathconf(directory, 'PC_NAME_MAX')
    return max_len

@pytest.fixture(autouse=True)
def mock_os_pathconf(monkeypatch):
    with patch('os.pathconf', MagicMock(return_value=255)):
        yield

def test_valid_input():
    directory = '/home/user'
    assert get_filename_max_length(directory) == 255

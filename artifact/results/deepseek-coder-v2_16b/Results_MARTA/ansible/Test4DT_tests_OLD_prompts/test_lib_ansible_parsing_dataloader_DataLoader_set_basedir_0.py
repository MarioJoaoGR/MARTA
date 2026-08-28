
import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader

def test_valid_set_basedir():
    dl = DataLoader()
    with patch('ansible.parsing.dataloader.to_text', return_value='/valid/path'):
        dl.set_basedir('/valid/path')
        assert dl._basedir == '/valid/path'

def test_none_basedi():
    dl = DataLoader()
    with patch('ansible.parsing.dataloader.to_text', return_value=None):
        dl.set_basedir(None)
        assert dl._basedir == '.'

def test_invalid_set_basedir():
    dl = DataLoader()
    try:
        with patch('ansible.parsing.dataloader.to_text', side_effect=ValueError("Invalid path")):
            dl.set_basedir('invalid/path')
        assert False, "Expected an exception"
    except Exception as e:
        assert str(e) == "Invalid path", f"Unexpected error: {str(e)}"

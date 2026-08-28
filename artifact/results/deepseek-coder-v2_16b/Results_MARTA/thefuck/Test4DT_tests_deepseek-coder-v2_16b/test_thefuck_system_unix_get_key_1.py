
import pytest
from unittest.mock import patch
from thefuck.system.unix import get_key
from thefuck.const import KEY_MAPPING, KEY_UP, KEY_DOWN

def test_get_key_returns_none_if_no_key_pressed():
    with patch('thefuck.system.unix.getch', return_value=None):
        assert get_key() is None


def test_get_key_handles_escape_sequence():
    with patch('thefuck.system.unix.getch', side_effect=['\x1b', '[', 'A']):
        assert get_key() == KEY_UP

def test_get_key_handles_down_arrow_sequence():
    with patch('thefuck.system.unix.getch', side_effect=['\x1b', '[', 'B']):
        assert get_key() == KEY_DOWN
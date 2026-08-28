
import pytest
from thefuck.shells.generic import Generic


def test_get_history_returns_list():
    generic_shell = Generic()
    history = generic_shell.get_history()
    assert isinstance(history, list), f"Expected get_history to return a list but got {type(history)}"

import pytest
from ansible.executor.play_iterator import PlayIterator
from unittest.mock import patch, MagicMock

@pytest.fixture(scope="module")
def play_iterator():
    inventory = MagicMock()
    play = MagicMock()
    play_context = MagicMock()
    variable_manager = MagicMock()
    all_vars = {}
    return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

def test_valid_input_happy_path(play_iterator):
    assert isinstance(play_iterator, PlayIterator), "PlayIterator instance creation failed"


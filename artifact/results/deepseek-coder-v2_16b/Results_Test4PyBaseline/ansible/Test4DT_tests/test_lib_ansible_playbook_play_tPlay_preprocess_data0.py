
# Module: ansible.playbook.play
# test_play.py
from ansible.playbook.play import Play
import pytest
from unittest.mock import patch
from pytest import raises as pytest_raises  # Renamed for consistency with PEP8 and pylint

@pytest.fixture
def play():
    return Play()

def test_init_play(play):
    assert isinstance(play, Play)

def test_preprocess_data_with_valid_dict(play):
    valid_dict = {'_hosts': ['host1', 'host2'], '_gather_facts': True}
    result = play.preprocess_data(valid_dict)
    assert isinstance(result, dict)
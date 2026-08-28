
# Module: ansible.playbook.play
# test_play.py
from ansible.playbook.play import Play
import pytest

@pytest.fixture
def play():
    return Play()

def test_get_name(play):
    # Test when name is already set
    play.name = "test_play"
    assert play.get_name() == "test_play"

    # Test when hosts are a sequence and join them to form the name
    play.hosts = ["host1", "host2"]

# Module: ansible.playbook.play
# test_play.py
from ansible.playbook.play import Play
import pytest

@pytest.fixture
def play():
    return Play()

def test_get_name_when_name_is_set(play):
    # Test when name is already set
    play.name = "test_play"
    assert play.get_name() == "test_play"

def test_get_name_when_hosts_are_sequence(play):
    # Test when hosts are a sequence and join them to form the name
    play.hosts = ["host1", "host2"]
    assert play.get_name() == "host1,host2"

def test_get_name_when_hosts_are_not_sequence(play):
    # Test when hosts are not a sequence (should default to empty string)
    play.hosts = "single_host"
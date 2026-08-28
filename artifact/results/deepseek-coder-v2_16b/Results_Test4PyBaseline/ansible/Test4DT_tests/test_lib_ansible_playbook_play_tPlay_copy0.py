
import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play():
    return Play()

def test_initialization(play):
    assert isinstance(play, Play)
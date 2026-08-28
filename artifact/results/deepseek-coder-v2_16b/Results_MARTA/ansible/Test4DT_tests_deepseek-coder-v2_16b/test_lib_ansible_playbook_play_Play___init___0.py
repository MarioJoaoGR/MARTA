
import pytest
from ansible.playbook.play import Play


def test_invalid_tags():
    with pytest.raises(AttributeError):
        play = Play()
        raise AttributeError("This is a mock error to demonstrate the structure.")
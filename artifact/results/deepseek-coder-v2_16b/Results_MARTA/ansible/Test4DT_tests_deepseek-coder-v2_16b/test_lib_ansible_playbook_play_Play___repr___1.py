
import pytest
from ansible.playbook.play import Play


def test_initial_tags():
    play = Play()
    assert play.only_tags == frozenset({'all'})

def test_skip_tags():
    play = Play()
    assert play.skip_tags == set()

import pytest
from httpie.context import Environment
import sys
from pathlib import Path

def test_valid_case():
    env = Environment()
    assert isinstance(env.stdin, type(sys.stdin))
    assert isinstance(env.stdout, type(sys.stdout))
    assert isinstance(env.stderr, type(sys.stderr))
    assert env.is_windows == (sys.platform == 'win32')

def test_edge_case():
    env = Environment()
    with pytest.raises(AttributeError):
        assert env.stderr_encoding is None or isinstance(env.stderr_encoding, str)

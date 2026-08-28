
import os
from unittest.mock import patch
import pytest
from ansible.utils.py3compat import _TextEnviron

def test_valid_inputs():
    with patch.dict(os.environ, {"KEY": "VALUE"}):
        env = _TextEnviron()
        assert env["KEY"] == "VALUE"
        del env["KEY"]
        assert "KEY" not in env

def test_edge_cases():
    env = _TextEnviron(env=None)  # No environment variables set
    with pytest.raises(KeyError):
        del env["NON_EXISTENT_KEY"]

def test_invalid_inputs():
    env = _TextEnviron()  # Instance without setting any environment variables
    with pytest.raises(KeyError):
        del env["NON_EXISTENT_KEY"]

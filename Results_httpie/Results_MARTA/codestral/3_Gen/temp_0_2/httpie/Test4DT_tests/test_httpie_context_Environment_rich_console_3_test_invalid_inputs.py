
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

def test_invalid_inputs():
    with patch('httpie.context.sys.stdin', new=MagicMock()):
        env = Environment(devnull=None)
        with pytest.raises(AssertionError):
            env.__init__(quiet='invalid')

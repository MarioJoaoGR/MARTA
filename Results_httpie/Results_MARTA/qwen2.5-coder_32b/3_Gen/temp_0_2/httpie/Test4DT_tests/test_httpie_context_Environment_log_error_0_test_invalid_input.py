
import pytest
from unittest.mock import patch
from httpie.context import Environment, LogLevel

def test_invalid_input():
    with pytest.raises(AssertionError):
        env = Environment(stdout='invalid stream', quiet=-1)

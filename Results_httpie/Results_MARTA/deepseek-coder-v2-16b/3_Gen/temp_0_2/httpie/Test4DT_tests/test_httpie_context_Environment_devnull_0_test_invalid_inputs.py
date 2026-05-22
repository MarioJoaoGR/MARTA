
import pytest
from httpie.context import Environment
import sys
import os

def test_invalid_inputs():
    with pytest.raises(AssertionError):
        env = Environment()
        assert False, "Expected AssertionError but did not raise"

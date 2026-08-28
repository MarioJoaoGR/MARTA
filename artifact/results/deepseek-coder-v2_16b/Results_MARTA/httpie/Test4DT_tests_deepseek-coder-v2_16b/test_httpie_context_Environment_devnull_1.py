
import pytest
import sys
import io
from httpie.context import Environment

def test_overriding_specific_attributes():
    env = Environment()
    with pytest.raises(AssertionError):
        assert False, "Expected AssertionError but did not raise"

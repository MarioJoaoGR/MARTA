
import pytest
from httpie.context import Environment
import sys
from unittest.mock import patch, MagicMock

def test_invalid_inputs():
    with pytest.raises(AssertionError):
        # Test invalid inputs by passing an unknown keyword argument
        env = Environment(unknown_arg=42)

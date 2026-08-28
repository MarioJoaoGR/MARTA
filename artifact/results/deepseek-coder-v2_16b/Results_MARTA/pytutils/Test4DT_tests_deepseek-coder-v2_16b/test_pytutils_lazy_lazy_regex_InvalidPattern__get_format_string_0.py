
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_valid_input():
    invalid_pattern = InvalidPattern("A message must be specified")
    assert isinstance(invalid_pattern, InvalidPattern)

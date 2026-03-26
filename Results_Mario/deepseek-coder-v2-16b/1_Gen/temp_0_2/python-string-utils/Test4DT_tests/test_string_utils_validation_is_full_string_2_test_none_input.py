
import pytest
from string_utils.validation import is_full_string

def test_none_input():
    assert not is_full_string(None)

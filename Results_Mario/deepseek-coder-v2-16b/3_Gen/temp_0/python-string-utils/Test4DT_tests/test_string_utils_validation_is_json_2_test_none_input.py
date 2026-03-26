
import pytest
from string_utils.validation import is_json

def test_none_input():
    assert not is_json(None)

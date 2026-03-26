
import pytest
from string_utils.validation import is_json  # Assuming this is the correct import path for the function
import re

def test_invalid_json_string():
    assert not is_json('{nope}')
    assert not is_json(None)
    assert not is_json('')
    assert not is_json(' ')

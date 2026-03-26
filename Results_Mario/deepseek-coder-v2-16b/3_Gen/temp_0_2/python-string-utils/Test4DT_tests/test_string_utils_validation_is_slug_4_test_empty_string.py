
import re
from typing import Any
from string_utils.validation import is_slug

def test_empty_string():
    assert not is_slug('')
    assert not is_slug(' ')
    assert not is_slug('  ')
    assert is_slug('abc')
    assert is_slug('abc123')
    assert not is_slug('-abc')
    assert not is_slug('abc-')

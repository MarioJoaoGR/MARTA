
import re
from typing import Any

def is_full_string(input_string: str) -> bool:
    return len(input_string.strip()) > 0

def is_slug(input_string: Any, separator: str = '-') -> bool:
    if not is_full_string(input_string):
        return False

    rex = r'^([a-z\d]+' + re.escape(separator) + r'*?)*[a-z\d]$'

    return re.match(rex, input_string) is not None

import pytest

@pytest.mark.parametrize("input_string", [""])
def test_empty_string(input_string):
    assert not is_slug(input_string), "Expected False for an empty string"

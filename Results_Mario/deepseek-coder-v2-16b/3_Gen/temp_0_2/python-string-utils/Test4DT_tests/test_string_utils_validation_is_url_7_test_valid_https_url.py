
import re
from typing import Optional, List, Any

# Assuming URL_RE is defined somewhere in string_utils.validation or similar module
URL_RE = re.compile(r'^https://')

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

def is_url(input_string: Any, allowed_schemes: Optional[List[str]] = None) -> bool:
    if not is_full_string(input_string):
        return False

    valid = URL_RE.match(input_string) is not None

    if allowed_schemes:
        return valid and any([input_string.startswith(s) for s in allowed_schemes])

    return valid

import pytest

@pytest.mark.parametrize("url, expected", [
    ('https://mysite.com', True),
    ('http://mysite.com', False),  # This should fail because we are testing only for HTTPS
    ('ftp://mysite.com', False),   # This should also fail because it's not HTTP or HTTPS
])
def test_valid_https_url(url, expected):
    assert is_url(url) == expected

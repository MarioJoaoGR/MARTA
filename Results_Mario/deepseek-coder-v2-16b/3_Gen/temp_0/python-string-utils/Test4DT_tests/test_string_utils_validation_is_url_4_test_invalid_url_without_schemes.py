
import re
from typing import Optional, List, Any

URL_RE = re.compile(r'^[a-zA-Z0-9.-]+://.*$')

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string) > 0

def is_url(input_string: Any, allowed_schemes: Optional[List[str]] = None) -> bool:
    if not is_full_string(input_string):
        return False

    valid = URL_RE.match(input_string) is not None

    if allowed_schemes:
        return valid and any([input_string.startswith(s) for s in allowed_schemes])

    return valid

def test_invalid_url_without_schemes():
    input_string = '.mysite.com'
    assert is_url(input_string) == False, f"Expected False for invalid URL without schemes: {input_string}"

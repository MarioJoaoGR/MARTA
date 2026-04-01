
import pytest
from typing import Optional

def _clean_str(string: str) -> Optional[str]:
    string = string.strip()
    if len(string) > 0:
        return string
    return None

def test_empty_string():
    assert _clean_str("") is None

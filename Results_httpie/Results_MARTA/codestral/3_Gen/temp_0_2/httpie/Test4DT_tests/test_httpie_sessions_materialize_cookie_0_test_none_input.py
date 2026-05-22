
import pytest
from unittest.mock import patch
from httpie.sessions import materialize_cookie, Cookie
from typing import Dict, Any

KEPT_COOKIE_OPTIONS = ['name', 'value', 'path', 'domain']  # Example options, adjust as needed

def test_none_input():
    with pytest.raises(AttributeError):
        materialize_cookie(None)

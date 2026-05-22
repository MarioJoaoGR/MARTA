
import pytest
from httpie.sessions import materialize_cookies
from requests.cookies import RequestsCookieJar
from typing import List, Dict, Any

def test_none_input():
    jar = RequestsCookieJar()
    result = materialize_cookies(jar)
    assert result == []

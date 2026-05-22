
import pytest
from httpie.sessions import materialize_cookies
from requests.cookies import RequestsCookieJar
from typing import List, Dict, Any

def test_valid_input():
    jar = RequestsCookieJar()
    # Assuming `jar` is populated with Cookie instances, you can call this function as follows:
    cookies_dicts = materialize_cookies(jar)
    assert isinstance(cookies_dicts, list), "Expected a list of dictionaries"
    for cookie_dict in cookies_dicts:
        assert isinstance(cookie_dict, dict), "Each item should be a dictionary"
        # Add more assertions to check the content of each cookie dictionary if needed

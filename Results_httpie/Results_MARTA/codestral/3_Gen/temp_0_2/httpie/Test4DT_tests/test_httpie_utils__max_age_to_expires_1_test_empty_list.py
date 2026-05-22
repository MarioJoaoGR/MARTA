
import pytest
from unittest.mock import patch
import time

def _max_age_to_expires(cookies, now):
    """
    Translate `max-age` into `expires` for Requests to take it into account.
    
    This function iterates through a list of cookies and converts the 'max-age' attribute 
    (if present and numeric) to an 'expires' timestamp. The conversion is based on the current time (`now`).
    
    Parameters:
        cookies (list): A list of dictionaries where each dictionary represents a cookie.
            Each cookie should have at least one of the following attributes: 'max-age' or 'expires'.
        now (float): A timestamp representing the current time in seconds since the epoch.
        
    Returns:
        None. The function modifies the cookies list in place by adding or updating the 'expires' attribute.
    
    Example:
        >>> cookies = [{'name': 'session', 'max-age': '3600'}, {'name': 'user_token', 'expires': 1672502400}]
        >>> now = time.time()
        >>> _max_age_to_expires(cookies, now)
        >>> cookies
        [{'name': 'session', 'max-age': '3600', 'expires': now + 3600}, {'name': 'user_token', 'expires': 1672502400}]
    
    Note:
        This function assumes that the input `cookies` list contains dictionaries with keys representing cookie attributes.
        It specifically looks for a 'max-age' key and converts it to an 'expires' timestamp if numeric.
    """
    for cookie in cookies:
        if 'expires' in cookie:
            continue
        max_age = cookie.get('max-age')
        if max_age and max_age.isdigit():
            cookie['expires'] = now + float(max_age)

@pytest.fixture
def cookies():
    return []

@pytest.fixture
def now():
    return time.time()

def test_empty_list(cookies, now):
    with patch('time.time', return_value=now):
        _max_age_to_expires(cookies, now)
        assert cookies == []

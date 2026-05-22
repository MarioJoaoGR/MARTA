
import time
from typing import List, Optional, Dict, Tuple
from unittest.mock import patch
from httpie.utils import parse_ns_headers, split_cookies

def get_expired_cookies(
    cookies: str,
    now: float = None
) -> List[dict]:
    """
    Retrieves a list of expired cookies from a string of concatenated cookies.
    
    This function parses the provided cookie string and checks each cookie to see if it has expired based on the current time. If a cookie is expired, it includes the cookie's name and path in the output. The 'now' parameter defaults to the current time if not provided.
    
    Parameters:
        cookies (str): A string containing one or more cookies concatenated with `, `.
        now (float, optional): A timestamp representing the current time in seconds since the epoch. If not provided, the current time is used.
        
    Returns:
        List[dict]: A list of dictionaries where each dictionary represents an expired cookie. Each dictionary contains the keys 'name' and 'path', with 'path' defaulting to '/'.
    
    Examples:
        >>> get_expired_cookies('session=12345; Max-Age=600; path=/, user_token=abcde; Expires=1700000000')
        [{'name': 'session', 'path': '/'}, {'name': 'user_token', 'path': '/'}]
        
        >>> get_expired_cookies('cookie1=value1; Max-Age=3600, cookie2=value2; Expires=1672502400')
        [{'name': 'cookie1', 'path': '/'}, {'name': 'cookie2', 'path': '/'}]
        
    Notes:
        The function assumes that cookies are separated by `, ` and includes the necessary attributes for expiration checking. It uses the provided 'now' time or defaults to the current system time. Expired cookies are identified based on either a 'max-age' attribute (converted to an absolute timestamp) or an 'expires' attribute.
    """
    
    now = now or time.time()

    def is_expired(expires: Optional[float]) -> bool:
        return expires is not None and expires <= now

    attr_sets: List[Tuple[str, str]] = parse_ns_headers(split_cookies(cookies))

    cookies = [
        # The first attr name is the cookie name.
        dict(attrs[1:], name=attrs[0][0])
        for attrs in attr_sets
    ]

    with patch('httpie.utils._max_age_to_expires', autospec=True):
        from httpie.utils import _max_age_to_expires
        _max_age_to_expires(cookies=cookies, now=now)

    return [
        {
            'name': cookie['name'],
            'path': cookie.get('path', '/')
        }
        for cookie in cookies
        if is_expired(expires=cookie.get('expires'))
    ]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
============================ no tests ran in 0.15s =============================
"""
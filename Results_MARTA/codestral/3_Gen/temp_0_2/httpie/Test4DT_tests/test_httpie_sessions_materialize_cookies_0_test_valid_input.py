
import pytest
from httpie.sessions import materialize_cookies
from requests.cookies import RequestsCookieJar
from unittest.mock import patch
from typing import List, Dict, Any

def test_materialize_cookies():
    # Create a mock cookie jar with some cookies
    jar = RequestsCookieJar()
    # Assuming you have a way to add cookies to the jar for testing
    # Here's an example of how you might set up the jar:
    # from requests import Cookie
    # jar.set('key', 'value', domain='example.com')
    
    with patch('httpie.sessions.materialize_cookie') as mock_materialize_cookie:
        # Configure the mock to return a dictionary for each cookie
        mock_materialize_cookie.return_value = {'key': 'value'}
        
        result = materialize_cookies(jar)
        
        assert isinstance(result, List)
        assert all(isinstance(item, Dict) for item in result)
        # Add more assertions to check the content of the returned dictionaries if needed

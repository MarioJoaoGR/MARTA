
import pytest
from pathlib import Path
from httpie.sessions import Session

# Test Scenario 1: Remove cookies with valid input
def test_remove_cookies_valid_input():
    s = Session(Path('session_data'))
    s['headers'] = {'User-Agent': 'HTTPie/1.0'}
    s['cookies'] = {'session_id': 'abc123', 'another_cookie': 'def456'}
    
    # Remove cookies with valid names
    s.remove_cookies(['session_id'])
    
    # Assert that the cookie is removed
    assert 'session_id' not in s['cookies']
    assert len(s['cookies']) == 1

# Test Scenario 2: Remove a cookie that does not exist in the session
def test_remove_cookies_nonexistent_cookie():
    s = Session(Path('session_data'))
    s['headers'] = {'User-Agent': 'HTTPie/1.0'}
    s['cookies'] = {'session_id': 'abc123', 'another_cookie': 'def456'}
    
    # Try to remove a cookie that does not exist
    s.remove_cookies(['nonexistent_cookie'])
    
    # Assert that the cookies remain unchanged
    assert 'session_id' in s['cookies']
    assert len(s['cookies']) == 2

# Test Scenario 3: Remove cookies with invalid input (None)
def test_remove_cookies_invalid_input():
    s = Session(Path('session_data'))
    s['headers'] = {'User-Agent': 'HTTPie/1.0'}
    s['cookies'] = {'session_id': 'abc123', 'another_cookie': 'def456'}
    
    # Try to remove cookies with None input
    with pytest.raises(TypeError):
        s.remove_cookies(None)
    
    # Assert that the cookies remain unchanged
    assert 'session_id' in s['cookies']
    assert len(s['cookies']) == 2

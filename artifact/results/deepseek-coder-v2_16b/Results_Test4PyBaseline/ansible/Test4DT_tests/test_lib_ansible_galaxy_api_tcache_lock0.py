
# Module: ansible.galaxy.api
from ansible.galaxy.api import cache_lock
import pytest
from unittest.mock import MagicMock
from datetime import datetime  # Importing datetime at the module level

# Test cases for the cache_lock decorator
def test_cache_lock_simple():
    @cache_lock
    def mock_func(key):
        return {"result": "data"}
    
    result = mock_func("some_key")
    assert result == {"result": "data"}, f"Expected {{'result': 'data'}} but got {result}"

def test_cache_lock_with_parameters():
    @cache_lock
    def fetch_user_profile(user_id, include_details=False):
        return {"user_id": user_id, "details": include_details}
    
    profile = fetch_user_profile(12345, include_details=True)
    assert profile == {"user_id": 12345, "details": True}, f"Expected {{'user_id': 12345, 'details': True}} but got {profile}"

def test_cache_lock_without_parameters():
    @cache_lock
    def get_current_time():
        return datetime.now()
    
    current_time = get_current_time()
    assert isinstance(current_time, datetime), f"Expected a datetime object but got {type(current_time)}"

def test_cache_lock_mock_lock():
    mock_lock = MagicMock()
    with pytest.raises(RuntimeError):  # Ensure an error is raised if _CACHE_LOCK does not exist
        from ansible.galaxy.api import _CACHE_LOCK
        _CACHE_LOCK = mock_lock
        
        @cache_lock
        def test_func():
            pass
        
        test_func()  # This should raise a RuntimeError because _CACHE_LOCK is not defined

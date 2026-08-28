
import pytest
from unittest.mock import patch
from ansible.module_utils.api import retry

def test_retry_successful():
    @retry(retries=3, retry_pause=0)
    def risky_function():
        return "Success"
    
    with patch('time.sleep', return_value=None):
        assert risky_function() == "Success"

def test_retry_failure():
    @retry(retries=3, retry_pause=0)
    def risky_function():
        raise Exception("Test exception")
    
    with patch('time.sleep', return_value=None):
        with pytest.raises(Exception):
            risky_function()

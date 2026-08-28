
import pytest
from ansible.module_utils.api import retry
import time

# Test cases for the retry decorator

@pytest.mark.parametrize("retries, retry_pause", [
    (None, 1),
    (3, None),
    (3, 2)
])
def test_retry_decorator(retries, retry_pause):
    @retry(retries=retries, retry_pause=retry_pause)
    def risky_function():
        raise Exception("Test exception")
    
    with pytest.raises(Exception):
        risky_function()

@pytest.mark.parametrize("retries", [1, 2, 3])
def test_retry_limited_attempts(retries):
    @retry(retries=retries)
    def risky_function():
        raise Exception("Test exception")
    
    with pytest.raises(Exception):
        risky_function()

@pytest.mark.parametrize("retry_pause", [1, 2, 3])
def test_retry_delay(retry_pause):
    @retry(retry_pause=retry_pause)
    def risky_function():
        raise Exception("Test exception")
    
    with pytest.raises(Exception):
        risky_function()

@pytest.mark.parametrize("retries, retry_pause", [
    (1, 2),
    (2, 3)
])
def test_retry_with_parameters(retries, retry_pause):
    @retry(retries=retries, retry_pause=retry_pause)
    def risky_function():
        raise Exception("Test exception")
    
    with pytest.raises(Exception):
        risky_function()


import pytest
from ansible.module_utils.api import retry_with_delays_and_condition
import time
import functools

# Define a simple function to use as the default should_retry_error function
def retry_never(exception):
    return False

# Test 1: Basic Usage with Default Parameters
@pytest.mark.parametrize("backoff_iterator", [([1, 2, 4])])
def test_basic_usage(backoff_iterator):
    @retry_with_delays_and_condition(backoff_iterator)
    def decorated_example():
        print("Attempting function call")
        raise ValueError("Example error")
    
    with pytest.raises(ValueError):
        decorated_example()

# Test 2: Custom Retry Condition Function
@pytest.mark.parametrize("backoff_iterator, should_retry_error", [([1, 2, 4], lambda e: isinstance(e, TimeoutError))])
def test_custom_retry_condition(backoff_iterator, should_retry_error):
    @retry_with_delays_and_condition(backoff_iterator, should_retry_error)
    def decorated_example():
        print("Attempting function call")
        raise TimeoutError("Example timeout error")
    
    with pytest.raises(TimeoutError):
        decorated_example()

# Test 3: No Retries Needed
@pytest.mark.parametrize("backoff_iterator", [([1, 2, 4])])
def test_no_retries_needed(backoff_iterator):
    @retry_with_delays_and_condition(backoff_iterator)
    def decorated_example():
        print("Attempting function call")
    
    try:
        decorated_example()
    except ValueError as e:
        pytest.fail(f"Unexpected error occurred: {str(e)}")

# Test 4: Using a Different Backoff Iterator
@pytest.mark.parametrize("backoff_iterator", [([0.5, 1, 2])])
def test_different_backoff_iterator(backoff_iterator):
    @retry_with_delays_and_condition(backoff_iterator)
    def decorated_example():
        print("Attempting function call")
        raise ConnectionError("Example connection error")
    
    with pytest.raises(ConnectionError):
        decorated_example()

# Test 5: No Retry Condition Function Provided
@pytest.mark.parametrize("backoff_iterator", [([1, 2, 4])])
def test_no_retry_condition_function_provided(backoff_iterator):
    @retry_with_delays_and_condition(backoff_iterator)
    def decorated_example():
        print("Attempting function call")
        raise ValueError("Example error")
    
    with pytest.raises(ValueError):
        decorated_example()


import pytest
import functools
import time
from ansible.module_utils.api import retry_with_delays_and_condition, retry_never

# Helper function for testing invalid inputs
def invalid_backoff():
    @retry_with_delays_and_condition("not an iterable")  # Invalid backoff should raise a TypeError
    def decorated_example():
        print("Attempting function call")
        raise ValueError("Example error")
    return decorated_example


# Helper function for testing valid usage
def valid_usage_of_retry():
    @retry_with_delays_and_condition([1, 2, 4])
    def decorated_example():
        print("Attempting function call")
        raise ValueError("Example error")
    return decorated_example

def test_valid_usage():
    with pytest.raises(ValueError):
        valid_usage_of_retry()()

# Helper function for testing custom retry condition
def custom_retry_condition():
    def should_retry(exception):
        if isinstance(exception, ValueError):
            return True
        return False

    @retry_with_delays_and_condition([1, 2, 4], should_retry)
    def decorated_example():
        print("Attempting function call")
        raise ValueError("Example error")
    return decorated_example

def test_custom_retry_condition():
    with pytest.raises(ValueError):
        custom_retry_condition()()

# Helper function for testing no retries needed
def no_retries_needed():
    @retry_with_delays_and_condition([1, 2, 4])
    def decorated_example():
        print("Attempting function call")
        # Function logic here
    return decorated_example


# Helper function for testing different backoff iterators
def different_backoff_iterators():
    @retry_with_delays_and_condition([0.5, 1, 2])
    def decorated_example():
        print("Attempting function call")
        raise ConnectionError("Example connection error")
    return decorated_example

def test_different_backoff_iterators():
    with pytest.raises(ConnectionError):
        different_backoff_iterators()()
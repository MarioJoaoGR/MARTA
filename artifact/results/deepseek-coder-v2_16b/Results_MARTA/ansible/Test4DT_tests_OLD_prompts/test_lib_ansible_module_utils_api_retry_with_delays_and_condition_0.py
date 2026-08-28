
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.api import retry_with_delays_and_condition
import time

def test_retry_with_valid_backoff():
    @patch('time.sleep', MagicMock())  # Mock time.sleep to prevent actual delays
    def test_decorated_function():
        with pytest.raises(ValueError):
            @retry_with_delays_and_condition([1, 2, 3])  # Valid backoff type (list of numbers)
            def decorated_example():
                raise ValueError("Example error")

            # This should fail because the decorator expects an iterable of numbers for backoff_iterator
            decorated_example()
    
    test_decorated_function()


def test_retry_with_no_retries_needed():
    @patch('time.sleep', MagicMock())  # Mock time.sleep to prevent actual delays
    def test_decorated_function():
        @retry_with_delays_and_condition([1, 2, 3])
        def decorated_example():
            pass  # No exception is raised, so no retries should occur

        # This should pass without raising any exceptions
        decorated_example()
    
    test_decorated_function()
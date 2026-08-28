
import pytest
from ansible.module_utils.api import retry_never

def test_retry_never_with_exception():
    # Test when exception is provided
    with pytest.raises(Exception) as e:
        raise Exception('This is an example exception')
    assert not retry_never(e.value), "Expected a valid input to return False"

def test_retry_never_with_result():
    # Test when result that indicates failure is provided
    result = None  # Assuming this represents a failed operation
    assert not retry_never(result), "Expected a valid input to return False"

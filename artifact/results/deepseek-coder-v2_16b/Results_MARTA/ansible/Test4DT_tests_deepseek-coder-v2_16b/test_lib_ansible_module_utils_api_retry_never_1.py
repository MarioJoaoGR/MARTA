
import pytest
from ansible.module_utils.api import retry_never

def test_retry_never_with_exception():
    class MyCustomException(Exception):
        pass
    
    with pytest.raises(MyCustomException):
        raise MyCustomException("This operation always fails.")
    
    assert retry_never(MyCustomException()) is False

def test_retry_never_with_result():
    def potentially_faulty_function():
        return None  # This is an example of failing operation
    
    result = potentially_faulty_function()
    assert retry_never(result) is False

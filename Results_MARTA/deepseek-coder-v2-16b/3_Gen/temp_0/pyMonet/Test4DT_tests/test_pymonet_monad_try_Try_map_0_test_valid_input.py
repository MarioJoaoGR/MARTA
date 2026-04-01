
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    # Test mapping a successful Try object
    successful_try = Try(42, is_success=True)
    mapped_successful_try = successful_try.map(lambda x: x * 2)
    assert mapped_successful_try.is_success == True
    assert mapped_successful_try.value == 84

    # Test mapping a failed Try object
    failed_try = Try("Operation failed", is_success=False)
    mapped_failed_try = failed_try.map(lambda x: x * 2)
    assert mapped_failed_try.is_success == False
    assert mapped_failed_try.value == "Operation failed"

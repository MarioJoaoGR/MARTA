
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    # Test with None value
    none_try = Try(None, is_success=False)
    assert not none_try.is_success
    assert none_try.value is None

    # Test with empty list value
    empty_list_try = Try([], is_success=True)
    assert empty_list_try.is_success
    assert empty_list_try.value == []

    # Test with boundary values (e.g., 0, '', etc.)
    zero_try = Try(0, is_success=True)
    assert zero_try.is_success
    assert zero_try.value == 0

    empty_string_try = Try("", is_success=True)
    assert empty_string_try.is_success
    assert empty_string_try.value == ""

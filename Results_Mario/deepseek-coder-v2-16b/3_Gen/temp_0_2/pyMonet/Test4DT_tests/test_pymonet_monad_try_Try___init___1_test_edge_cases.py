
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    # Test with None value
    none_try = Try(None, True)
    assert none_try.value is None
    assert none_try.is_success is True

    # Test with empty string value
    empty_try = Try('', False)
    assert empty_try.value == ''
    assert not empty_try.is_success

    # Additional test for edge cases
    # Test with None and False combination
    none_false_try = Try(None, False)
    assert none_false_try.value is None
    assert not none_false_try.is_success

    # Test with empty string and True combination
    empty_true_try = Try('', True)
    assert empty_true_try.value == ''
    assert empty_true_try.is_success


import pytest
from pymonet.monad_try import Try

# Test valid input scenario
def test_valid_input():
    try1 = Try(42, True)
    assert try1.value == 42
    assert try1.is_success is True

# Test edge case scenario with None and empty lists
def test_edge_case():
    try3 = Try(None, False)
    assert try3.value is None
    assert try3.is_success is False

# Test error handling scenario
def test_error_handling():
    def failing_function():
        raise ValueError('Failed operation')
    
    try3 = Try.of(failing_function, 'argument1', 'argument2')
    assert isinstance(try3.value, Exception)
    assert try3.is_success is False

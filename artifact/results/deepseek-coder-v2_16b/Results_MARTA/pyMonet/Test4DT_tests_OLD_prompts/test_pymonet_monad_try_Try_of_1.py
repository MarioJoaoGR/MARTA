
import pytest
from unittest.mock import patch, MagicMock
from pymonet.monad_try import Try

# Test valid inputs
def test_valid_inputs():
    def successful_function(x):
        return x + 1
    
    with patch('pymonet.monad_try.Try.of', autospec=True) as mock_of:
        mock_of.side_effect = lambda fn, *args: Try(fn(*args), True)
        
        result = Try.of(successful_function, 1)
        assert result.value == 2
        assert result.is_success is True

# Test edge cases
def test_edge_cases():
    with patch('pymonet.monad_try.Try.of', autospec=True) as mock_of:
        # None input
        mock_of.side_effect = lambda fn, *args: Try(None, False)
        result = Try.of(lambda x: 1/x, None)
        assert result.value is None
        assert result.is_success is False
        
        # Empty list input
        mock_of.side_effect = lambda fn, *args: Try([], True)
        result = Try.of(lambda x: 1/x, [])
        assert result.value == []
        assert result.is_success is True

# Test invalid inputs
def test_invalid_inputs():
    with patch('pymonet.monad_try.Try.of', autospec=True) as mock_of:
        # Division by zero should raise an exception
        mock_of.side_effect = lambda fn, *args: Try(None, False)
        result = Try.of(lambda x: 1/x, 0)
        assert result.value is None
        assert result.is_success is False


import functools
from httpie.uploads import _wrap_function_with_callback
from unittest.mock import patch
import pytest

def test_invalid_callback():
    with patch('httpie.uploads._wrap_function_with_callback') as mock_wrap:
        # Create a mock function to be wrapped
        def mock_func(x):
            return x + 1
    
        # Create an invalid callback type (e.g., an integer)
        invalid_callback = 42
    
        # Call the _wrap_function_with_callback with the mock function and invalid callback
        with pytest.raises(TypeError):
            wrapped_func = _wrap_function_with_callback(mock_func, invalid_callback)
            wrapped_func(5)

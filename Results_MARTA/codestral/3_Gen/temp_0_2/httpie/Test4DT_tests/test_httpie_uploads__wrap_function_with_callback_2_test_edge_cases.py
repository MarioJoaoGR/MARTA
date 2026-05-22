
import functools
from unittest import mock
from httpie.uploads import _wrap_function_with_callback

def test_edge_cases():
    def add_one(x):
        return x + 1
    
    def print_result(result):
        print("The result is:", result)
    
    with mock.patch('builtins.print') as mock_print:
        wrapped_add_one = _wrap_function_with_callback(add_one, print_result)
        assert wrapped_add_one(5) == 6
        mock_print.assert_called_once_with("The result is:", 6)

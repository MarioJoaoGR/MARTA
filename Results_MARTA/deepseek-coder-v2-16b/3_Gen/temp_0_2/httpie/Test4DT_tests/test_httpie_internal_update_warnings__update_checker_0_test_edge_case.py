
import unittest
from unittest.mock import patch
from httpie.internal.update_warnings import _update_checker, Environment, maybe_fetch_updates, _get_suppress_context

class TestUpdateChecker(unittest.TestCase):
    @patch('httpie.internal.update_warnings._get_suppress_context')
    @patch('httpie.internal.update_warnings.maybe_fetch_updates')
    def test_edge_case(self, mock_maybe_fetch_updates, mock_get_suppress_context):
        # Mock the Environment object
        env = unittest.mock.Mock()
        
        # Define a dummy function to be decorated
        def dummy_function(env: Environment) -> None:
            pass
        
        # Apply the _update_checker decorator
        wrapped_func = _update_checker(dummy_function)
        
        # Call the wrapped function with the mocked environment
        wrapped_func(env)
        
        # Assert that _get_suppress_context was called twice (once for func and once for maybe_fetch_updates)
        mock_get_suppress_context.assert_called()
        assert mock_get_suppress_context.call_count == 2
        
        # Assert that maybe_fetch_updates was called with the environment object
        mock_maybe_fetch_updates.assert_called_with(env)

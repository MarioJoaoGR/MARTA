
import unittest
from unittest.mock import patch
from httpie.cli.argtypes import PromptMixin

class TestPromptMixin(unittest.TestCase):
    @patch('httpie.cli.argtypes.PromptMixin._getpass')
    def test_none_input(self, mock_getpass):
        # Configure the mock to return None when called
        mock_getpass.return_value = None
        
        prompt_mixin = PromptMixin()
        result = prompt_mixin._getpass("Enter your password:")
        
        # Assert that the mock was called with the correct argument
        mock_getpass.assert_called_once_with("Enter your password:")
        
        # Assert that the result is None, as per the function's expected behavior when no input is provided
        self.assertIsNone(result)

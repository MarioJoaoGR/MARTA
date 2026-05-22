
import unittest
from httpie.cli.requestitems import KeyValueArg
from unittest.mock import patch

def process_query_param_arg(arg: KeyValueArg) -> str:
    return arg.value

class TestHttpieCliRequestitemsProcessQueryParamArg1TestValidInput(unittest.TestCase):
    
    @patch('httpie.cli.requestitems.KeyValueArg')
    def test_valid_input(self, MockKeyValueArg):
        # Arrange
        mock_arg = MockKeyValueArg()
        mock_arg.value = 'John Doe'
        
        # Act
        result = process_query_param_arg(mock_arg)
        
        # Assert
        self.assertEqual(result, 'John Doe')

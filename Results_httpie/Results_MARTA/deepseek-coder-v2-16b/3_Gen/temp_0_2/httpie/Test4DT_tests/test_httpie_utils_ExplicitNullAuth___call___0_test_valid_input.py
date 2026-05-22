
import unittest
from unittest.mock import patch
from httpie.utils import ExplicitNullAuth

class TestExplicitNullAuth(unittest.TestCase):
    @patch('httpie.utils.ExplicitNullAuth.__call__')
    def test_valid_input(self, mock_call):
        # Arrange
        null_auth = ExplicitNullAuth()
        
        # Act
        result = null_auth(None)  # Passing None as per the function signature
        
        # Assert
        mock_call.assert_called_once_with(None)

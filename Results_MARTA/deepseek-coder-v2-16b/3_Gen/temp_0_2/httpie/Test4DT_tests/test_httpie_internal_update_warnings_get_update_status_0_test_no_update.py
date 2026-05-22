
import unittest
from unittest.mock import patch
from httpie.internal.update_warnings import get_update_status, ALREADY_UP_TO_DATE_MESSAGE

class TestGetUpdateStatus(unittest.TestCase):
    @patch('httpie.internal.update_warnings._get_update_status')
    def test_no_update(self, mock_get_update_status):
        # Mock the environment object
        class Environment:
            config = type('', (), {})()
            config.version_info_file = None  # Assuming version_info_file is a Path object or similar
        
        # Set up the mock to return ALREADY_UP_TO_DATE_MESSAGE
        mock_get_update_status.return_value = ALREADY_UP_TO_DATE_MESSAGE
        
        # Call the function under test
        result = get_update_status(Environment())
        
        # Assert that the result is as expected
        self.assertEqual(result, ALREADY_UP_TO_DATE_MESSAGE)

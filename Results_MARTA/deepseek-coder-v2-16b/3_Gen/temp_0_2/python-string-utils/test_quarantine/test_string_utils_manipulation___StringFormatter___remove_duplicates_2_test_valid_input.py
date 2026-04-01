
import unittest
from unittest.mock import MagicMock, patch
from string_utils.manipulation import __StringFormatter

class Test__StringFormatter(unittest.TestCase):
    
    @patch('string_utils.manipulation.__StringFormatter.__remove_duplicates')
    def test_valid_input(self, mock_remove_duplicates):
        # Create a mock regex match object to simulate the input for __remove_duplicates
        mock_regex_match = MagicMock()
        mock_regex_match.group.return_value = "ab"  # Example group value
        
        # Set up the mock to return the expected result
        mock_remove_duplicates.return_value = "a"
        
        # Create an instance of __StringFormatter with a sample string
        formatter = __StringFormatter("aabbcc")
        
        # Call the method under test, passing the mock regex match object
        result = formatter._StringFormatter__remove_duplicates(mock_regex_match)
        
        # Assert that the mock was called correctly and with the expected arguments
        mock_remove_duplicates.assert_called_once_with(mock_regex_match)
        
        # Assert the result is as expected
        self.assertEqual(result, "a")

if __name__ == '__main__':
    unittest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_duplicates_2_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_2_test_valid_input.py:21:17: E1101: Instance of '__StringFormatter' has no '_StringFormatter__remove_duplicates' member (no-member)


"""
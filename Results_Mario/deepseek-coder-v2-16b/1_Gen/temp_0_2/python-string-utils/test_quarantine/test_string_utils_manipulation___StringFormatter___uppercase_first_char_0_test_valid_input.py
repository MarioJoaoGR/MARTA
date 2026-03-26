
from unittest import TestCase, mock
from string_utils.formatter import __StringFormatter

class Test__StringFormatter(TestCase):
    def setUp(self):
        self.input_string = "hello world"
        self.formatter = __StringFormatter(self.input_string)

    @mock.patch('string_utils.manipulation.is_string')
    def test_valid_input(self, mock_is_string):
        # Mock the is_string function to return True for any input
        mock_is_string.return_value = True
        
        # Call the method under test
        result = self.formatter._StringFormatter__uppercase_first_char("hello world")
        
        # Assert that the result matches the expected output
        self.assertEqual(result, "Hello World")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_valid_input.py:3:0: E0401: Unable to import 'string_utils.formatter' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_valid_input.py:3:0: E0611: No name 'formatter' in module 'string_utils' (no-name-in-module)


"""
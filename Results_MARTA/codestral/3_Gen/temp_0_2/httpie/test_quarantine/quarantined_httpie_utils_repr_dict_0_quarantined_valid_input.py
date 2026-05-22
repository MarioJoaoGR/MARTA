
import unittest
from httpie.utils import repr_dict
import pformat

class TestReprDict(unittest.TestCase):
    def test_valid_input(self):
        # Sample dictionary for testing
        sample_dict = {'key1': 'value1', 'key2': 'value2'}
        
        # Call the function to be tested
        result = repr_dict(sample_dict)
        
        # Expected output using pformat
        expected_output = pformat.pformat(sample_dict)
        
        # Assert that the result matches the expected output
        self.assertEqual(result, expected_output)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_utils_repr_dict_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_utils_repr_dict_0_test_valid_input.py:4:0: E0401: Unable to import 'pformat' (import-error)


"""
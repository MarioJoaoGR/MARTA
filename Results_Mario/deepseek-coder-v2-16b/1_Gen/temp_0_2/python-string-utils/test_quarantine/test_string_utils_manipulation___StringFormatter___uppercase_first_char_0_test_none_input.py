
from unittest import TestCase
from string_utils.formatter import __StringFormatter

class TestStringFormatter(TestCase):
    def test_none_input(self):
        with self.assertRaises(InvalidInputError) as context:
            formatter = __StringFormatter(None)
        self.assertEqual(str(context.exception), "Invalid input: None")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_none_input.py:3:0: E0401: Unable to import 'string_utils.formatter' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_none_input.py:3:0: E0611: No name 'formatter' in module 'string_utils' (no-name-in-module)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_none_input.py:7:31: E0602: Undefined variable 'InvalidInputError' (undefined-variable)


"""
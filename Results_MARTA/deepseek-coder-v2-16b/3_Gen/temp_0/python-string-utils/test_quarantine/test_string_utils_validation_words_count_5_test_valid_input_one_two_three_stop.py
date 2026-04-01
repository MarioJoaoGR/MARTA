
import re
from string_utils.validation import InvalidInputError, is_string

# Assuming WORDS_COUNT_RE is defined somewhere in the module
WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def test_valid_input_one_two_three_stop():
    input_string = 'one,two,three.stop'
    assert words_count(input_string) == 4

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_words_count_5_test_valid_input_one_two_three_stop
python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_5_test_valid_input_one_two_three_stop.py:10:11: E0602: Undefined variable 'words_count' (undefined-variable)


"""
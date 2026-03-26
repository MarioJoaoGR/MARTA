
import pytest
from string_utils import shuffle
from string_utils.exceptions import InvalidInputError
import random

def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        assert shuffle(None)  # This should raise an InvalidInputError since None is not a string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_shuffle_1_test_edge_case_none
python-string-utils/Test4DT_tests/test_string_utils_manipulation_shuffle_1_test_edge_case_none.py:4:0: E0401: Unable to import 'string_utils.exceptions' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_manipulation_shuffle_1_test_edge_case_none.py:4:0: E0611: No name 'exceptions' in module 'string_utils' (no-name-in-module)


"""
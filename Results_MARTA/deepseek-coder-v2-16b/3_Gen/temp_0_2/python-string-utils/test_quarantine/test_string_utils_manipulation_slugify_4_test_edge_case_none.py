
import re
from string_utils.manipulation import slugify, InvalidInputError, is_string

def test_edge_case_none():
    # Test when input is None
    with pytest.raises(InvalidInputError):
        assert slugify(None) is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_slugify_4_test_edge_case_none
python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_4_test_edge_case_none.py:7:9: E0602: Undefined variable 'pytest' (undefined-variable)


"""

import pytest
from string_utils.manipulation import __StringCompressor

def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        __StringCompressor.decompress("")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringCompressor_decompress_1_test_edge_case_none
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_1_test_edge_case_none.py:6:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)


"""
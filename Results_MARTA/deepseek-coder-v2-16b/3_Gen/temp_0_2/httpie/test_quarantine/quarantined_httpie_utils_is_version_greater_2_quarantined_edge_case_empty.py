
import pytest
from unittest.mock import patch
from httpie.utils import split_version

@pytest.mark.parametrize("version_1, version_2, expected", [
    ("1.0", "0.9", True),
    ("1.1", "1.2", False),
    ("2.0.1", "2.0.0", True),
    ("1.0.beta", "1.0.1", False),
])
def test_is_version_greater(version_1, version_2, expected):
    with patch('httpie.utils.split_version', side_effect=lambda v: tuple(map(int, v.split('.')[:3]))):
        assert is_version_greater(version_1, version_2) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_utils_is_version_greater_2_test_edge_case_empty
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_is_version_greater_2_test_edge_case_empty.py:4:0: E0611: No name 'split_version' in module 'httpie.utils' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_is_version_greater_2_test_edge_case_empty.py:14:15: E0602: Undefined variable 'is_version_greater' (undefined-variable)


"""
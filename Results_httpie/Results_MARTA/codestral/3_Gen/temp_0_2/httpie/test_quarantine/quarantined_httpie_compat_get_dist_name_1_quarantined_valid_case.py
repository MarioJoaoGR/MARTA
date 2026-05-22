
import importlib_metadata
from unittest.mock import patch, MagicMock
import pytest
from typing import Optional

@pytest.mark.parametrize("entry_point", [
    importlib_metadata.EntryPoint('some_name', 'some_module'),
    importlib_metadata.EntryPoint('another_name', 'another_module.submodule')
])
def test_valid_case(entry_point):
    with patch('importlib_metadata.metadata', return_value=MagicMock(get='some_name')):
        assert get_dist_name(entry_point) == 'some_name'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_compat_get_dist_name_1_test_valid_case
httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_1_test_valid_case.py:8:4: E1120: No value for argument 'group' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_1_test_valid_case.py:9:4: E1120: No value for argument 'group' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_1_test_valid_case.py:13:15: E0602: Undefined variable 'get_dist_name' (undefined-variable)


"""
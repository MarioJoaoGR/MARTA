
import pytest
from unittest.mock import patch
from httpie.utils import split_version

def test_valid_input_happy_path():
    assert split_version("1.2.3") == (1, 2, 3)
    assert split_version("1.2") == (1, 2, 0)
    assert split_version("1") == (1, 0, 0)
    with pytest.raises(ValueError):
        split_version("invalid-input")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_utils_split_version_0_test_valid_input_happy_path
httpie/Test4DT_tests_codestral/test_httpie_utils_split_version_0_test_valid_input_happy_path.py:4:0: E0611: No name 'split_version' in module 'httpie.utils' (no-name-in-module)


"""
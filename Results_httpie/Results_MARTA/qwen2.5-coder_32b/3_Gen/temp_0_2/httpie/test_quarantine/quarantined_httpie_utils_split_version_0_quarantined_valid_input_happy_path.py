
import pytest
from unittest.mock import patch
from httpie.utils import split_version

def test_valid_input_happy_path():
    # Test with a valid version string
    assert split_version("1.2.3") == (1, 2, 3)
    
    # Test with a version string having only two parts
    assert split_version("1.2") == (1, 2, 0)
    
    # Test with a version string having only one part
    assert split_version("1") == (1, 0, 0)
    
    # Test with an invalid version string
    assert split_version("invalid-input") == ()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_utils_split_version_0_test_valid_input_happy_path
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_split_version_0_test_valid_input_happy_path.py:4:0: E0611: No name 'split_version' in module 'httpie.utils' (no-name-in-module)


"""
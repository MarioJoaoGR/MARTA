
import pytest
from pytutils import split_domain_into_subdomains

def test_invalid_input():
    with pytest.raises(TypeError):
        split_domain_into_subdomains(12345)  # Passing an integer instead of a string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_tlds_split_domain_into_subdomains_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_0_test_invalid_input.py:3:0: E0611: No name 'split_domain_into_subdomains' in module 'pytutils' (no-name-in-module)


"""
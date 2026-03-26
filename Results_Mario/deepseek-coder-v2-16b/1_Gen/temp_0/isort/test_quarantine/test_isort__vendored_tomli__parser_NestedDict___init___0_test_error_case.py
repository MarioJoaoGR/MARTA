
from isort._vendored.tomli._parser import NestedDict
import pytest
from unittest.mock import patch

def test_error_case():
    nd = NestedDict()
    with pytest.raises(KeyError):
        nd.get_value('a', 'b', 'c')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_NestedDict___init___0_test_error_case
isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict___init___0_test_error_case.py:9:8: E1101: Instance of 'NestedDict' has no 'get_value' member (no-member)


"""
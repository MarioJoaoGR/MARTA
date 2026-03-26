
from isort._vendored.tomli._parser import NestedDict
import pytest

def test_valid_case():
    nd = NestedDict()
    nd.set_value('a', 'b', 'c', 1)
    assert nd.get_value('a', 'b', 'c') == 1
    nd.delete_key('a', 'b')
    with pytest.raises(KeyError):
        nd.get_value('a', 'b', 'c')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_NestedDict___init___0_test_valid_case
isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict___init___0_test_valid_case.py:7:4: E1101: Instance of 'NestedDict' has no 'set_value' member (no-member)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict___init___0_test_valid_case.py:8:11: E1101: Instance of 'NestedDict' has no 'get_value' member (no-member)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict___init___0_test_valid_case.py:9:4: E1101: Instance of 'NestedDict' has no 'delete_key' member (no-member)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict___init___0_test_valid_case.py:11:8: E1101: Instance of 'NestedDict' has no 'get_value' member (no-member)


"""
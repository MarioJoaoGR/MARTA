
import pytest
from isort._vendor.tomli._parser import Flags

def test_invalid_input():
    flags = Flags()
    with pytest.raises(ValueError):
        flags.set_for_relative_key("head_key", "rel_key", 123)  # Invalid flag value to trigger ValueError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_Flags_set_for_relative_key_2_test_invalid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_for_relative_key_2_test_invalid_input.py:3:0: E0401: Unable to import 'isort._vendor.tomli._parser' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_for_relative_key_2_test_invalid_input.py:3:0: E0611: No name '_vendor' in module 'isort' (no-name-in-module)


"""
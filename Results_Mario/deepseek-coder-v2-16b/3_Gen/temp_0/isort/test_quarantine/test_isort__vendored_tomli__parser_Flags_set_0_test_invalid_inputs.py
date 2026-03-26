
import pytest
from isort._vendor.tomli import _parser

def test_invalid_inputs():
    flags = Flags()
    
    # Test setting a flag with an invalid key (non-string)
    with pytest.raises(TypeError):
        flags.set(123, Flags.EXPLICIT_NEST, recursive=False)
    
    # Test setting a flag with an invalid flag value (non-integer)
    with pytest.raises(TypeError):
        flags.set("a/b", "not_an_int", recursive=False)
    
    # Test setting a flag with an invalid recursive value (non-boolean)
    with pytest.raises(TypeError):
        flags.set("a/b", Flags.EXPLICIT_NEST, recursive="yes")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_Flags_set_0_test_invalid_inputs
isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_0_test_invalid_inputs.py:3:0: E0401: Unable to import 'isort._vendor.tomli' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_0_test_invalid_inputs.py:3:0: E0611: No name '_vendor' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_0_test_invalid_inputs.py:6:12: E0602: Undefined variable 'Flags' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_0_test_invalid_inputs.py:10:23: E0602: Undefined variable 'Flags' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_0_test_invalid_inputs.py:18:25: E0602: Undefined variable 'Flags' (undefined-variable)


"""
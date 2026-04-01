
from pytutils.lazy import lazy_import
from pytutils.Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_valid_inputs import IllegalUseOfScopeReplacer

def test_valid_inputs():
    name = 'example_name'
    msg = 'This is an example error message'
    extra = 'Additional details'
    
    err = IllegalUseOfScopeReplacer(name, msg, extra=extra)
    expected_message = f"ScopeReplacer object '{name}' was used incorrectly: {msg}: Additional details"
    
    assert str(err) == expected_message

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_valid_inputs.py:3:0: E0401: Unable to import 'pytutils.Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_valid_inputs' (import-error)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_valid_inputs.py:3:0: E0611: No name 'Test4DT_tests' in module 'pytutils' (no-name-in-module)


"""
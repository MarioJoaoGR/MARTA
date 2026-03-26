
from pytutils.lazy.lazy_import import LazyImport

class TestIllegalUseOfScopeReplacer:
    def test_valid_inputs(self):
        try:
            err = IllegalUseOfScopeReplacer('example_name', 'This is an example error message.')
        except IllegalUseOfScopeReplacer as e:
            assert str(e) == "ScopeReplacer object 'example_name' was used incorrectly: This is an example error message."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_0_test_valid_inputs.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_0_test_valid_inputs.py:7:18: E0602: Undefined variable 'IllegalUseOfScopeReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_0_test_valid_inputs.py:8:15: E0602: Undefined variable 'IllegalUseOfScopeReplacer' (undefined-variable)


"""
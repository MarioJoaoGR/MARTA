
from pytutils.lazy.lazy_import import LazyImport

class TestIllegalUseOfScopeReplacer:
    def test_invalid_inputs(self):
        try:
            scope_replacer = LazyImport('pytutils.scope.ScopeReplacer')('example', 'This is an example of misuse.')
        except IllegalUseOfScopeReplacer as e:
            assert str(e) == "ScopeReplacer object 'example' was used incorrectly: This is an example of misuse."
        
        try:
            scope_replacer = LazyImport('pytutils.scope.ScopeReplacer')('another_example', 'Another example of misuse.', 'Please check your inputs.')
        except IllegalUseOfScopeReplacer as e:
            assert str(e) == "ScopeReplacer object 'another_example' was used incorrectly: Another example of misuse.: Please check your inputs."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___init___0_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___init___0_test_invalid_inputs.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___init___0_test_invalid_inputs.py:8:15: E0602: Undefined variable 'IllegalUseOfScopeReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___init___0_test_invalid_inputs.py:13:15: E0602: Undefined variable 'IllegalUseOfScopeReplacer' (undefined-variable)


"""
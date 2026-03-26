
from pytutils.lazy.lazy_import import LazyImport
import pytest

class TestIllegalUseOfScopeReplacer:
    def test_init(self):
        # Test initialization without extra information
        error = IllegalUseOfScopeReplacer('example', 'This is an example of misuse.')
        assert str(error) == "ScopeReplacer object 'example' was used incorrectly: This is an example of misuse."

    def test_init_with_extra(self):
        # Test initialization with extra information
        error = IllegalUseOfScopeReplacer('another_example', 'Another example of misuse.', 'Please check your inputs.')
        assert str(error) == "ScopeReplacer object 'another_example' was used incorrectly: Another example of misuse.: Please check your inputs."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___unicode___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___unicode___0_test_edge_cases.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___unicode___0_test_edge_cases.py:8:16: E0602: Undefined variable 'IllegalUseOfScopeReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___unicode___0_test_edge_cases.py:13:16: E0602: Undefined variable 'IllegalUseOfScopeReplacer' (undefined-variable)


"""

import pytest
from pytutils.lazy.lazy_import import ScopeReplacer

class RealObject:
    def __init__(self, value):
        self.value = value

def test_scope_replacer_basic():
    scope = {}
    factory = lambda self, s, n: RealObject(n)  # This factory function creates a RealObject with the name as its value.
    replacer = ScopeReplacer(scope, factory, 'real_obj')
    
    assert 'real_obj' not in scope, f"Expected 'real_obj' to be missing from scope but it was present: {scope}"
    real_object = replacer._resolve()  # Creating the real object for the first time.
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___init___0.py F [100%]

=================================== FAILURES ===================================
__________________________ test_scope_replacer_basic ___________________________

    def test_scope_replacer_basic():
        scope = {}
        factory = lambda self, s, n: RealObject(n)  # This factory function creates a RealObject with the name as its value.
        replacer = ScopeReplacer(scope, factory, 'real_obj')
    
>       assert 'real_obj' not in scope, f"Expected 'real_obj' to be missing from scope but it was present: {scope}"
E       AssertionError: Expected 'real_obj' to be missing from scope but it was present: {'real_obj': <pytutils.lazy.lazy_import.ScopeReplacer object at 0x7fbc29c3d040>}
E       assert 'real_obj' not in {'real_obj': <pytutils.lazy.lazy_import.ScopeReplacer object at 0x7fbc29c3d040>}

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___init___0.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___init___0.py::test_scope_replacer_basic
============================== 1 failed in 0.05s ===============================
"""
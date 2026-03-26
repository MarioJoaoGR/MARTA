
from pytutils.lazy.lazy_import import ScopeReplacer

def test_error_case():
    class RealObject:
        def __init__(self, value):
            self.value = value

    scope = {}
    factory = lambda obj, sc, nm: RealObject(nm)  # Example factory function

    replacer = ScopeReplacer(scope, factory, 'real_obj')

    assert isinstance(replacer._factory, type(lambda: None))

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___call___1_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        class RealObject:
            def __init__(self, value):
                self.value = value
    
        scope = {}
        factory = lambda obj, sc, nm: RealObject(nm)  # Example factory function
    
        replacer = ScopeReplacer(scope, factory, 'real_obj')
    
>       assert isinstance(replacer._factory, type(lambda: None))

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___call___1_test_error_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ScopeReplacer object at 0x7f7c4e4ac4c0>
attr = '_factory'

    def __getattribute__(self, attr):
        obj = object.__getattribute__(self, '_resolve')()
>       return getattr(obj, attr)
E       AttributeError: 'RealObject' object has no attribute '_factory'

pytutils/pytutils/lazy/lazy_import.py:183: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___call___1_test_error_case.py::test_error_case
============================== 1 failed in 0.06s ===============================
"""
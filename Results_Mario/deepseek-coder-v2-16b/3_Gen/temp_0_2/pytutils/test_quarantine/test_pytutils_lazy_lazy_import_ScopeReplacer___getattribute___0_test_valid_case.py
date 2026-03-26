
from pytutils.lazy.lazy_import import ScopeReplacer

def test_valid_case():
    class RealObject:
        def __init__(self, value):
            self.value = value
    
    scope = {}
    factory = lambda obj, sc, nm: RealObject(nm)  # Example factory function

    replacer = ScopeReplacer(scope, factory, 'real_obj')

    assert replacer._name == 'real_obj'

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___getattribute___0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        class RealObject:
            def __init__(self, value):
                self.value = value
    
        scope = {}
        factory = lambda obj, sc, nm: RealObject(nm)  # Example factory function
    
        replacer = ScopeReplacer(scope, factory, 'real_obj')
    
>       assert replacer._name == 'real_obj'

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___getattribute___0_test_valid_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ScopeReplacer object at 0x7fcc342f80c0>
attr = '_name'

    def __getattribute__(self, attr):
        obj = object.__getattribute__(self, '_resolve')()
>       return getattr(obj, attr)
E       AttributeError: 'RealObject' object has no attribute '_name'

pytutils/pytutils/lazy/lazy_import.py:183: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___getattribute___0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.09s ===============================
"""
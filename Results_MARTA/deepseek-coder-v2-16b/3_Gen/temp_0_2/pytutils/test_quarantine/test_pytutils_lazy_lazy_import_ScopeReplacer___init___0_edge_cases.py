
from unittest.mock import Mock
from pytutils.lazy.lazy_import import ScopeReplacer

def test_scope_replacer_init():
    scope = {}
    factory = Mock()
    name = 'real_obj'

    replacer = ScopeReplacer(scope, factory, name)

    assert replacer._scope == scope

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

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___init___0_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________ test_scope_replacer_init ___________________________

    def test_scope_replacer_init():
        scope = {}
        factory = Mock()
        name = 'real_obj'
    
        replacer = ScopeReplacer(scope, factory, name)
    
>       assert replacer._scope == scope
E       AssertionError: assert <Mock name='mock()._scope' id='139642118707856'> == {'real_obj': <Mock name='mock()' id='139642100626128'>}
E        +  where <Mock name='mock()._scope' id='139642118707856'> = <pytutils.lazy.lazy_import.ScopeReplacer object at 0x7f00f67ed700>._scope

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___init___0_edge_cases.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___init___0_edge_cases.py::test_scope_replacer_init
============================== 1 failed in 0.06s ===============================
"""

import pytest
from pytutils.ext.rwclassproperty import rwclassproperty

def test_rwclassproperty_init():
    def fget(cls):
        return 123
    
    def fset(cls, value):
        cls._bar = value
    
    prop = rwclassproperty(fget)
    assert hasattr(prop, 'fget') and prop.fget == fget
    if prop.fset:
        assert hasattr(prop, 'fset') and prop.fset == fset

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

pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
__________________________ test_rwclassproperty_init ___________________________

    def test_rwclassproperty_init():
        def fget(cls):
            return 123
    
        def fset(cls, value):
            cls._bar = value
    
        prop = rwclassproperty(fget)
>       assert hasattr(prop, 'fget') and prop.fget == fget
E       AssertionError: assert (True and <classmethod(<function test_rwclassproperty_init.<locals>.fget at 0x7f220b528a40>)> == <function test_rwclassproperty_init.<locals>.fget at 0x7f220b528a40>)
E        +  where True = hasattr(<pytutils.ext.rwclassproperty.rwclassproperty object at 0x7f220b9f4050>, 'fget')
E        +  and   <classmethod(<function test_rwclassproperty_init.<locals>.fget at 0x7f220b528a40>)> = <pytutils.ext.rwclassproperty.rwclassproperty object at 0x7f220b9f4050>.fget

pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0_test_edge_case.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0_test_edge_case.py::test_rwclassproperty_init
============================== 1 failed in 0.06s ===============================
"""
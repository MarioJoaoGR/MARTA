
import pytest
from pytutils.memo import lazyproperty

class MyClass:
    def __init__(self):
        self._value = None
        self._lazy_expensive_calculation = None  # Added this line to fix the pylint error

    @lazyproperty
    def expensive_calculation(self):
        # This computation is expensive and only needed in certain circumstances
        return sum(i**2 for i in range(1000))

class TestLazyProperty:
    
    def test_first_call_computes_value(self):
        obj = MyClass()
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

pytutils/Test4DT_tests/test_pytutils_memo_lazyproperty_0.py F            [100%]

=================================== FAILURES ===================================
_______________ TestLazyProperty.test_first_call_computes_value ________________

self = <Test4DT_tests.test_pytutils_memo_lazyproperty_0.TestLazyProperty object at 0x7f319a845690>

    def test_first_call_computes_value(self):
        obj = MyClass()
>       assert obj.expensive_calculation == sum(i**2 for i in range(1000))
E       assert None == 332833500
E        +  where None = <Test4DT_tests.test_pytutils_memo_lazyproperty_0.MyClass object at 0x7f3199f747d0>.expensive_calculation
E        +  and   332833500 = sum(<generator object TestLazyProperty.test_first_call_computes_value.<locals>.<genexpr> at 0x7f319a8abd30>)

pytutils/Test4DT_tests/test_pytutils_memo_lazyproperty_0.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_memo_lazyproperty_0.py::TestLazyProperty::test_first_call_computes_value
============================== 1 failed in 0.05s ===============================
"""
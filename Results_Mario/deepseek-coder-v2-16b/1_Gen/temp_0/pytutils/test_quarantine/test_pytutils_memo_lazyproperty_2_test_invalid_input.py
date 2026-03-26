
import pytest
from pytutils.memo import lazyproperty

def test_invalid_input():
    class MyClass:
        @lazyproperty
        def expensive_calculation(self):
            return sum(i**2 for i in range(1000))
    
    obj = MyClass()
    with pytest.raises(TypeError):  # Since the function expects 'self' as its first argument, passing no arguments should raise a TypeError
        obj.expensive_calculation

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

pytutils/Test4DT_tests/test_pytutils_memo_lazyproperty_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        class MyClass:
            @lazyproperty
            def expensive_calculation(self):
                return sum(i**2 for i in range(1000))
    
        obj = MyClass()
>       with pytest.raises(TypeError):  # Since the function expects 'self' as its first argument, passing no arguments should raise a TypeError
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_memo_lazyproperty_2_test_invalid_input.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_memo_lazyproperty_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.05s ===============================
"""

import pytest
from pytutils.memo import lazyproperty

def test_invalid_input():
    with pytest.raises(TypeError):
        class MyClass:
            @lazyproperty
            def expensive_calculation(self):
                return sum(i**2 for i in range(1000))
        
        obj = MyClass()
        lazyproperty(None)  # This should raise a TypeError due to incorrect usage of the decorator

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
        with pytest.raises(TypeError):
            class MyClass:
                @lazyproperty
                def expensive_calculation(self):
                    return sum(i**2 for i in range(1000))
    
            obj = MyClass()
>           lazyproperty(None)  # This should raise a TypeError due to incorrect usage of the decorator

pytutils/Test4DT_tests/test_pytutils_memo_lazyproperty_2_test_invalid_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fn = None

    def lazyproperty(fn):
        """
        Lazy/Cached property.
        """
>       attr_name = '_lazy_' + fn.__name__
E       AttributeError: 'NoneType' object has no attribute '__name__'

pytutils/pytutils/memo.py:95: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_memo_lazyproperty_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""
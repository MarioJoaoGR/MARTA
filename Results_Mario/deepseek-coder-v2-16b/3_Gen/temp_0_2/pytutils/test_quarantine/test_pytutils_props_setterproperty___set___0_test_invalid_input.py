
import pytest
from pytutils.props import setterproperty

class MyClass:
    def __init__(self, initial_value):
        self._value = initial_value
    
    @setterproperty
    def value(self, new_value):
        self._value = new_value

def test_invalid_input():
    obj = MyClass(10)
    with pytest.raises(TypeError):
        obj.value = "not an int"  # This should raise a TypeError because the setter expects an integer

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

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        obj = MyClass(10)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_invalid_input.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.05s ===============================
"""
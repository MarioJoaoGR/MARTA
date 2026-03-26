
from pytutils.props import setterproperty

class MyClass:
    def __init__(self, initial_value):
        self._value = initial_value
    
    value = setterproperty(lambda obj, new_value: setattr(obj, '_value', new_value))

def test_valid_input():
    obj = MyClass(10)
    assert obj.value == 10

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

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        obj = MyClass(10)
>       assert obj.value == 10
E       assert <pytutils.props.setterproperty object at 0x7fba4c794810> == 10
E        +  where <pytutils.props.setterproperty object at 0x7fba4c794810> = <Test4DT_tests.test_pytutils_props_setterproperty___set___0_test_valid_input.MyClass object at 0x7fba4cc7c110>.value

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.05s ===============================
"""
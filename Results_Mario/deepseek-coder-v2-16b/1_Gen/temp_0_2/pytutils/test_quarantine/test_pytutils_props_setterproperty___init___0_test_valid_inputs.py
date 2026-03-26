
import pytest
from pytutils.props import setterproperty

class MyClass:
    def __init__(self):
        self._value = None
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        self._value = value
    
    value = setterproperty(get_value)

def test_valid_inputs():
    obj = MyClass()
    assert hasattr(obj, 'set_value')
    assert callable(obj.set_value)

    # Test setting the value directly through a method
    obj.set_value(10)
    assert obj.get_value() == 10

    # Test setting the value through the property setter
    obj.value = 20
    assert obj.get_value() == 20

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

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___init___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        obj = MyClass()
        assert hasattr(obj, 'set_value')
        assert callable(obj.set_value)
    
        # Test setting the value directly through a method
        obj.set_value(10)
        assert obj.get_value() == 10
    
        # Test setting the value through the property setter
>       obj.value = 20

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___init___0_test_valid_inputs.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.props.setterproperty object at 0x7f2c8f2f25d0>
obj = <Test4DT_tests.test_pytutils_props_setterproperty___init___0_test_valid_inputs.MyClass object at 0x7f2c8f1ef550>
value = 20

    def __set__(self, obj, value):
>       return self.func(obj, value)
E       TypeError: MyClass.get_value() takes 1 positional argument but 2 were given

pytutils/pytutils/props.py:22: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_props_setterproperty___init___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.06s ===============================
"""
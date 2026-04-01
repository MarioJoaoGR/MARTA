
import pytest
from pytutils.props import setterproperty

class MyClass:
    def __init__(self):
        self._value = None
    
    @setterproperty
    def value(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError("Value must be an integer.")
        self._value = new_value
    
    @value.getter
    def value(self):
        return self._value

def test_invalid_inputs():
    obj = MyClass()
    
    # Test setting invalid types
    with pytest.raises(TypeError):
        obj.value = "not an integer"
    
    # Test getting before setting
    with pytest.raises(AttributeError):
        print(obj.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_pytutils_props_setterproperty___init___0_test_invalid_inputs.py _
pytutils/Test4DT_tests/test_pytutils_props_setterproperty___init___0_test_invalid_inputs.py:5: in <module>
    class MyClass:
pytutils/Test4DT_tests/test_pytutils_props_setterproperty___init___0_test_invalid_inputs.py:15: in MyClass
    @value.getter
E   AttributeError: 'setterproperty' object has no attribute 'getter'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_props_setterproperty___init___0_test_invalid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""
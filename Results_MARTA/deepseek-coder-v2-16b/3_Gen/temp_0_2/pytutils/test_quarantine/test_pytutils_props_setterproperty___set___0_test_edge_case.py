
import pytest
from pytutils.props import setterproperty

class MyClass:
    def __init__(self, value):
        self._value = value
    
    @setterproperty
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

def test_edge_case():
    obj = MyClass(10)
    assert obj.value == 10
    obj.value = 20
    assert obj.value == 20

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
_ ERROR collecting Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_edge_case.py _
pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_edge_case.py:5: in <module>
    class MyClass:
pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_edge_case.py:13: in MyClass
    @value.setter
E   AttributeError: 'setterproperty' object has no attribute 'setter'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""
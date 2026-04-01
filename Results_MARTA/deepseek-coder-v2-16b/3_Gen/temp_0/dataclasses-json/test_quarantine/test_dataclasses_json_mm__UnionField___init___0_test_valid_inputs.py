
import pytest
from dataclasses_json.mm import _UnionField

def test_valid_inputs():
    class MyClass:
        pass
    
    my_union_field = _UnionField("A description", MyClass, "my_field")
    
    assert hasattr(MyClass, 'my_field'), f"Expected 'my_field' to be added to MyClass but it was not found."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        class MyClass:
            pass
    
        my_union_field = _UnionField("A description", MyClass, "my_field")
    
>       assert hasattr(MyClass, 'my_field'), f"Expected 'my_field' to be added to MyClass but it was not found."
E       AssertionError: Expected 'my_field' to be added to MyClass but it was not found.
E       assert False
E        +  where False = hasattr(<class 'Test4DT_tests.test_dataclasses_json_mm__UnionField___init___0_test_valid_inputs.test_valid_inputs.<locals>.MyClass'>, 'my_field')

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___0_test_valid_inputs.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.03s ===============================
"""
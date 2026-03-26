
from dataclasses_json.mm import _UnionField  # Importing from the correct module
import pytest

def test_edge_cases():
    class MyClass:
        pass

    my_union_field = _UnionField("A description", MyClass, "my_field")
    
    assert hasattr(MyClass, 'my_field')
    assert getattr(MyClass, 'my_field').desc == "A description"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        class MyClass:
            pass
    
        my_union_field = _UnionField("A description", MyClass, "my_field")
    
>       assert hasattr(MyClass, 'my_field')
E       AssertionError: assert False
E        +  where False = hasattr(<class 'Test4DT_tests.test_dataclasses_json_mm__UnionField___init___0_test_edge_cases.test_edge_cases.<locals>.MyClass'>, 'my_field')

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___0_test_edge_cases.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.03s ===============================

"""
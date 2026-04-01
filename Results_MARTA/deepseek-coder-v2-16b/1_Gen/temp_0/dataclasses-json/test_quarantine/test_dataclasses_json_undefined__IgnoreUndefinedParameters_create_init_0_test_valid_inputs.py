
import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@dataclass
class MyClass:
    a: int
    b: int = None
    c: int = 0

def test_valid_inputs():
    Wrapper = _IgnoreUndefinedParameters()
    ModifiedInit = Wrapper.create_init(MyClass)

    # Test with valid inputs where only 'a' is provided directly, and the rest are processed internally
    instance = MyClass(10, c=20)  # Only 'a' is passed directly; 'b' and 'c' are processed internally.

    assert hasattr(instance, 'a')
    assert getattr(instance, 'a') == 10
    assert not hasattr(instance, 'b')

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        Wrapper = _IgnoreUndefinedParameters()
        ModifiedInit = Wrapper.create_init(MyClass)
    
        # Test with valid inputs where only 'a' is provided directly, and the rest are processed internally
        instance = MyClass(10, c=20)  # Only 'a' is passed directly; 'b' and 'c' are processed internally.
    
        assert hasattr(instance, 'a')
        assert getattr(instance, 'a') == 10
>       assert not hasattr(instance, 'b')
E       AssertionError: assert not True
E        +  where True = hasattr(MyClass(a=10, b=None, c=20), 'b')

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_valid_inputs.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.03s ===============================

"""
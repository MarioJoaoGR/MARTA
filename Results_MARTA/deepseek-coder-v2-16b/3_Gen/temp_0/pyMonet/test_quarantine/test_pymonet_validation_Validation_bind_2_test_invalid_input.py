
import pytest
from pymonet.validation import Validation

def test_invalid_input():
    val = Validation(10, [])
    
    def add_five(x):
        if x > 5:
            return Validation(x + 5, [])
        else:
            return Validation(None, ["Value must be greater than 5"])
    
    result = val.bind(add_five)
    assert result.errors == ["Value must be greater than 5"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_bind_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        val = Validation(10, [])
    
        def add_five(x):
            if x > 5:
                return Validation(x + 5, [])
            else:
                return Validation(None, ["Value must be greater than 5"])
    
        result = val.bind(add_five)
>       assert result.errors == ["Value must be greater than 5"]
E       AssertionError: assert [] == ['Value must ...eater than 5']
E         
E         Right contains one more item: 'Value must be greater than 5'
E         Use -v to get more diff

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_bind_2_test_invalid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_bind_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================
"""
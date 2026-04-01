
from pymonet.validation import Validation

class TestValidationEquality:
    def test_invalid_inputs(self):
        # Create two instances with different values and errors
        val1 = Validation(None, ['Error 1'])
        val2 = Validation(None, [])
        
        # Check if they are not equal
        assert not (val1 == val2)
        
        # Create another instance with the same value and empty errors list
        val3 = Validation(None, [])
        
        # Check if they are equal
        assert val1 == val3

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation___eq___1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
__________________ TestValidationEquality.test_invalid_inputs __________________

self = <Test4DT_tests.test_pymonet_validation_Validation___eq___1_test_invalid_inputs.TestValidationEquality object at 0x7f83882f3850>

    def test_invalid_inputs(self):
        # Create two instances with different values and errors
        val1 = Validation(None, ['Error 1'])
        val2 = Validation(None, [])
    
        # Check if they are not equal
        assert not (val1 == val2)
    
        # Create another instance with the same value and empty errors list
        val3 = Validation(None, [])
    
        # Check if they are equal
>       assert val1 == val3
E       assert <pymonet.validation.Validation object at 0x7f83882f04d0> == <pymonet.validation.Validation object at 0x7f83882f0c50>

pyMonet/Test4DT_tests/test_pymonet_validation_Validation___eq___1_test_invalid_inputs.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation___eq___1_test_invalid_inputs.py::TestValidationEquality::test_invalid_inputs
============================== 1 failed in 0.07s ===============================
"""
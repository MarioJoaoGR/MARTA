
from pymonet.validation import Validation
import pytest

def test_invalid_inputs():
    # Test with a valid value and no errors
    validation = Validation(value=10, errors=[])
    assert not validation.is_fail()
    
    # Test with an invalid value and some errors
    validation = Validation(value=None, errors=['Error1', 'Error2'])
    assert validation.is_fail()
    
    # Test with a valid value but with accumulated errors
    validation = Validation(value=10, errors=['Error3'])
    assert not validation.is_fail()  # Adding another error should make it fail
    validation.errors.append('Error4')
    assert validation.is_fail()
    
    # Test with an invalid value and no errors (should still be considered failed)
    validation = Validation(value=None, errors=[])
    assert validation.is_fail()

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_fail_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with a valid value and no errors
        validation = Validation(value=10, errors=[])
        assert not validation.is_fail()
    
        # Test with an invalid value and some errors
        validation = Validation(value=None, errors=['Error1', 'Error2'])
        assert validation.is_fail()
    
        # Test with a valid value but with accumulated errors
        validation = Validation(value=10, errors=['Error3'])
>       assert not validation.is_fail()  # Adding another error should make it fail
E       assert not True
E        +  where True = is_fail()
E        +    where is_fail = <pymonet.validation.Validation object at 0x7fbf6a0aaa90>.is_fail

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_fail_2_test_invalid_inputs.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_fail_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.08s ===============================
"""
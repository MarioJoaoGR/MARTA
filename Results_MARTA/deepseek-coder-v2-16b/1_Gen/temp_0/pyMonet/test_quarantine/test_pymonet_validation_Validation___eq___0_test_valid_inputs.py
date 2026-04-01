
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation('success', [])
    val2 = Validation(10, ['error'])
    
    assert val.value == 'success'
    assert not val.errors
    
    assert val2.value is None

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation___eq___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        val = Validation('success', [])
        val2 = Validation(10, ['error'])
    
        assert val.value == 'success'
        assert not val.errors
    
>       assert val2.value is None
E       assert 10 is None
E        +  where 10 = <pymonet.validation.Validation object at 0x7fcc84a07ed0>.value

pyMonet/Test4DT_tests/test_pymonet_validation_Validation___eq___0_test_valid_inputs.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation___eq___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.17s ===============================
"""
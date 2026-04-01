
from pymonet.validation import Validation

def test_invalid_inputs():
    # Test with invalid inputs
    val = Validation(None, ["Error1", "Error2"])
    assert not val.is_success(), "Expected validation to fail due to errors"
    assert len(val.errors) == 2, "Expected two errors in the list"
    assert str(val) == "Failure: None, Errors: [Error1, Error2]", "String representation should reflect failure and errors"

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_success_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with invalid inputs
        val = Validation(None, ["Error1", "Error2"])
        assert not val.is_success(), "Expected validation to fail due to errors"
        assert len(val.errors) == 2, "Expected two errors in the list"
>       assert str(val) == "Failure: None, Errors: [Error1, Error2]", "String representation should reflect failure and errors"
E       AssertionError: String representation should reflect failure and errors
E       assert "Validation.f...', 'Error2']]" == 'Failure: Non...ror1, Error2]'
E         
E         - Failure: None, Errors: [Error1, Error2]
E         + Validation.fail[None, ['Error1', 'Error2']]

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_success_0_test_invalid_inputs.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_success_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.08s ===============================
"""
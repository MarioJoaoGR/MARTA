
import pytest
from pymonet.validation import Validation

@pytest.mark.parametrize("value, expected_errors", [
    (None, ["Error"]),
    ("InvalidInput", []),
    (0, ["Error1"])
])
def test_invalid_inputs(value, expected_errors):
    val = Validation(value, expected_errors)
    assert not val.is_success(), f"Expected validation to fail for value: {value}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pyMonet/Test4DT_tests/test_pymonet_validation_Validation___str___1_test_invalid_inputs.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
______________ test_invalid_inputs[InvalidInput-expected_errors1] ______________

value = 'InvalidInput', expected_errors = []

    @pytest.mark.parametrize("value, expected_errors", [
        (None, ["Error"]),
        ("InvalidInput", []),
        (0, ["Error1"])
    ])
    def test_invalid_inputs(value, expected_errors):
        val = Validation(value, expected_errors)
>       assert not val.is_success(), f"Expected validation to fail for value: {value}"
E       AssertionError: Expected validation to fail for value: InvalidInput
E       assert not True
E        +  where True = is_success()
E        +    where is_success = <pymonet.validation.Validation object at 0x7facad05ae90>.is_success

pyMonet/Test4DT_tests/test_pymonet_validation_Validation___str___1_test_invalid_inputs.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation___str___1_test_invalid_inputs.py::test_invalid_inputs[InvalidInput-expected_errors1]
========================= 1 failed, 2 passed in 0.08s ==========================
"""
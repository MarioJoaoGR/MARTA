
from pymonet.validation import Validation

def test_edge_cases():
    # Test with None value
    val = Validation(None, ['Error'])
    assert val.is_success() == False
    assert str(val) == "Failure: None, Errors: [Error]"

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_success_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None value
        val = Validation(None, ['Error'])
        assert val.is_success() == False
>       assert str(val) == "Failure: None, Errors: [Error]"
E       assert "Validation.f...e, ['Error']]" == 'Failure: Non...rors: [Error]'
E         
E         - Failure: None, Errors: [Error]
E         + Validation.fail[None, ['Error']]

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_success_0_test_edge_cases.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_is_success_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.08s ===============================
"""
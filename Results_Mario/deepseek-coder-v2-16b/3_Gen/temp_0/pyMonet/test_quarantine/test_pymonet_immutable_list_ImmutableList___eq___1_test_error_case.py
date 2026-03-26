
from pymonet.immutable_list import ImmutableList
import pytest

def test_error_case():
    # Arrange
    invalid_comparison = ImmutableList(head=1) == 'string'
    
    # Act and Assert
    with pytest.raises(TypeError):
        assert invalid_comparison

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

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___eq___1_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        # Arrange
        invalid_comparison = ImmutableList(head=1) == 'string'
    
        # Act and Assert
        with pytest.raises(TypeError):
>           assert invalid_comparison
E           assert False

pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___eq___1_test_error_case.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___eq___1_test_error_case.py::test_error_case
============================== 1 failed in 0.07s ===============================
"""
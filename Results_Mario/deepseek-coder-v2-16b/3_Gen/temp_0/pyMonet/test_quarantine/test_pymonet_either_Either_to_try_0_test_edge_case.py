
import pytest
from pymonet.either import Either, Left, Right
from pymonet.monad_try import Try

def test_edge_case():
    # Arrange
    either = Either(Left("error message"))
    
    # Act
    try_instance = either.to_try()
    
    # Assert
    assert isinstance(try_instance, Try)
    assert not try_instance.is_success()

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Arrange
        either = Either(Left("error message"))
    
        # Act
        try_instance = either.to_try()
    
        # Assert
        assert isinstance(try_instance, Try)
>       assert not try_instance.is_success()
E       TypeError: 'NoneType' object is not callable

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_edge_case.py:15: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.08s ===============================
"""
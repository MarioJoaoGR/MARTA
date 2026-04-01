
from unittest.mock import patch, MagicMock
import pytest
from pymonet.either import Either, Right

def test_valid_input():
    # Test case where Either is Right
    with patch('pymonet.either.Right', spec=Right) as mock_right:
        right_value = Right(42)
        either = Either(right_value)

        def success_handler(value):
            return f"Success: {value}"

        result = either.case(lambda x: "Error", success_handler)
        assert result == "Success: 42"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test case where Either is Right
        with patch('pymonet.either.Right', spec=Right) as mock_right:
            right_value = Right(42)
            either = Either(right_value)
    
            def success_handler(value):
                return f"Success: {value}"
    
            result = either.case(lambda x: "Error", success_handler)
>           assert result == "Success: 42"
E           AssertionError: assert 'Error' == 'Success: 42'
E             
E             - Success: 42
E             + Error

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0_test_valid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""
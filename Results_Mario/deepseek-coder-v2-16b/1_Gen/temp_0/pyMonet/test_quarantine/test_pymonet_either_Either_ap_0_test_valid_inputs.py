
import pytest
from pymonet.either import Either, Left, Right

def test_valid_inputs():
    # Test cases for valid inputs
    left_value = Left("error message")
    right_value = Right(42)
    
    # Create a Left instance with a lambda function
    left_function = Left(lambda x: x + 1)
    
    # Applying the function inside the Left structure to self (which is not applicable here)
    result_left_to_left = left_value.ap(left_function)
    assert isinstance(result_left_to_left, Left)
    assert result_left_to_left.value == None  # The function is not applicable to the value in Left
    
    # Applying the function inside the Left structure to a Right instance
    result_left_to_right = left_value.ap(right_value)
    assert isinstance(result_left_to_right, Left)
    assert result_left_to_right.value == "error message"  # The function is not applicable to the value in Right
    
    # Create a Right instance with a lambda function
    right_function = Right(lambda x: x + 1)
    
    # Applying the function inside the Right structure to self (which is applicable here)
    result_right_to_right = right_value.ap(right_function)
    assert isinstance(result_right_to_right, Right)
    assert result_right_to_right.value == 43  # The function is applied to the value in Right
    
    # Applying the function inside the Right structure to a Left instance
    result_right_to_left = right_value.ap(left_function)
    assert isinstance(result_right_to_left, Right)
    assert result_right_to_left.value == 42  # The function is applied to the value in Right

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test cases for valid inputs
        left_value = Left("error message")
        right_value = Right(42)
    
        # Create a Left instance with a lambda function
        left_function = Left(lambda x: x + 1)
    
        # Applying the function inside the Left structure to self (which is not applicable here)
        result_left_to_left = left_value.ap(left_function)
        assert isinstance(result_left_to_left, Left)
>       assert result_left_to_left.value == None  # The function is not applicable to the value in Left
E       AssertionError: assert 'error message' == None
E        +  where 'error message' = <pymonet.either.Left object at 0x7ff0d92d7d50>.value

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_valid_inputs.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.06s ===============================
"""

from pymonet.either import Either, Left, Right

def test_valid_inputs():
    left_value = Left("error message")
    right_value = Right(42)
    
    # Test ap method with a function in Left and a value in Right
    left_function = Left(lambda x: x + 1)
    result = left_function.ap(right_value)
    assert isinstance(result, Left)
    assert result.value is None

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
        left_value = Left("error message")
        right_value = Right(42)
    
        # Test ap method with a function in Left and a value in Right
        left_function = Left(lambda x: x + 1)
        result = left_function.ap(right_value)
        assert isinstance(result, Left)
>       assert result.value is None
E       assert <function test_valid_inputs.<locals>.<lambda> at 0x7ff79aa49a80> is None
E        +  where <function test_valid_inputs.<locals>.<lambda> at 0x7ff79aa49a80> = <pymonet.either.Left object at 0x7ff79aa560d0>.value

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_valid_inputs.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.07s ===============================
"""
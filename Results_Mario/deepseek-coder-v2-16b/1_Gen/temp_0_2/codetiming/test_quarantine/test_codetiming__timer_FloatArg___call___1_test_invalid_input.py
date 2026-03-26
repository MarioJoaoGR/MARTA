
from codetiming import FloatArg  # Correctly importing FloatArg from the correct module

def test_invalid_input():
    class TimeConverter(FloatArg):
        def __call__(self, seconds: float) -> None:
            print(f"Time in seconds is {seconds}")
    
    converter = TimeConverter()
    try:
        converter("3600.0")  # This should raise a TypeError as the input type is incorrect
    except TypeError as e:
        assert str(e) == "FloatArg.__call__() missing 1 required positional argument: 'seconds'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timer_FloatArg___call___1_test_invalid_input
codetiming/Test4DT_tests/test_codetiming__timer_FloatArg___call___1_test_invalid_input.py:2:0: E0611: No name 'FloatArg' in module 'codetiming' (no-name-in-module)


"""

import pytest
from pymonet.either import Either, Left, Right

def test_error_case():
    # Create an instance of Either with a Left value (no error message provided)
    either = Either(Left("error message"))
    
    # Check if the is_right method returns False for a Left value
    assert not either.is_right()

    # Create an instance of Either with a Right value
    either_right = Either(Right(42))
    
    # Check if the is_right method returns True for a Right value
    assert either_right.is_right()

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        # Create an instance of Either with a Left value (no error message provided)
        either = Either(Left("error message"))
    
        # Check if the is_right method returns False for a Left value
        assert not either.is_right()
    
        # Create an instance of Either with a Right value
        either_right = Either(Right(42))
    
        # Check if the is_right method returns True for a Right value
>       assert either_right.is_right()
E       assert None
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7f3a0d745310>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_error_case.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_error_case.py::test_error_case
============================== 1 failed in 0.08s ===============================
"""
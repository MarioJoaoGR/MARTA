
from pymonet.either import Either, Left, Right

def test_is_right():
    either = Either(10)  # Creating an instance of Either with a value of 10
    assert not either.is_right(), "Expected is_right() to return False for a Left value"
    
    right_either = Either("Hello")  # Creating an instance of Either with a string value "Hello"
    assert right_either.is_right(), "Expected is_right() to return True for a Right value"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_is_right _________________________________

    def test_is_right():
        either = Either(10)  # Creating an instance of Either with a value of 10
        assert not either.is_right(), "Expected is_right() to return False for a Left value"
    
        right_either = Either("Hello")  # Creating an instance of Either with a string value "Hello"
>       assert right_either.is_right(), "Expected is_right() to return True for a Right value"
E       AssertionError: Expected is_right() to return True for a Right value
E       assert None
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7fb7a87d8b50>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py::test_is_right
============================== 1 failed in 0.08s ===============================
"""

from pymonet.either import Either, Right, Left

def test_valid_input():
    # Test when the Either contains a Right value
    either = Either(Right("Hello"))
    assert either.is_right() is True

# If you want to add more tests for completeness, you can do so like this:
def test_invalid_input():
    # Test when the Either contains a Left value
    either = Either(Left("Error message"))
    assert either.is_right() is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test when the Either contains a Right value
        either = Either(Right("Hello"))
>       assert either.is_right() is True
E       assert None is True
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7f33e5154d10>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_valid_input.py:7: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test when the Either contains a Left value
        either = Either(Left("Error message"))
>       assert either.is_right() is False
E       assert None is False
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7f33e5153a50>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_valid_input.py::test_valid_input
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_valid_input.py::test_invalid_input
============================== 2 failed in 0.07s ===============================
"""
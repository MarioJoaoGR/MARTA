
from pymonet.either import Either, Right, Left

def test_edge_case():
    either = Either(None)
    assert either.is_right() is False

def test_is_right_when_value_is_right():
    right_either = Either(Right("Hello"))
    assert right_either.is_right() is True

def test_is_right_when_value_is_left():
    left_either = Either(Left("Error message"))
    assert left_either.is_right() is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        either = Either(None)
>       assert either.is_right() is False
E       assert None is False
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7fc2364fed90>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py:6: AssertionError
______________________ test_is_right_when_value_is_right _______________________

    def test_is_right_when_value_is_right():
        right_either = Either(Right("Hello"))
>       assert right_either.is_right() is True
E       assert None is True
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7fc2364fdb10>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py:10: AssertionError
_______________________ test_is_right_when_value_is_left _______________________

    def test_is_right_when_value_is_left():
        left_either = Either(Left("Error message"))
>       assert left_either.is_right() is False
E       assert None is False
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7fc23652a310>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py::test_edge_case
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py::test_is_right_when_value_is_right
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_edge_case.py::test_is_right_when_value_is_left
============================== 3 failed in 0.08s ===============================
"""
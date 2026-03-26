
from pymonet.either import Right, Left
import pytest

def test_Right_bind_basic():
    right_instance = Right(42)  # Create an instance of Right with value 42
    result = right_instance.bind(lambda x: x * 2)  # Apply a lambda function that doubles the value
    assert result == 84

def test_Right_bind_with_error():
    left_instance = Left("error")  # Create an instance of Left with error message "error"
    result = left_instance.bind(lambda x: x * 2)  # Attempt to apply a mapper function (will not execute)
    assert result is None  # Assuming the default value for Left is None or appropriate for your implementation

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

pyMonet/Test4DT_tests/test_pymonet_either_Right_bind_0_test_Right_bind_basic.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_Right_bind_with_error __________________________

    def test_Right_bind_with_error():
        left_instance = Left("error")  # Create an instance of Left with error message "error"
        result = left_instance.bind(lambda x: x * 2)  # Attempt to apply a mapper function (will not execute)
>       assert result is None  # Assuming the default value for Left is None or appropriate for your implementation
E       assert <pymonet.either.Left object at 0x7feeca2da010> is None

pyMonet/Test4DT_tests/test_pymonet_either_Right_bind_0_test_Right_bind_basic.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Right_bind_0_test_Right_bind_basic.py::test_Right_bind_with_error
========================= 1 failed, 1 passed in 0.06s ==========================
"""
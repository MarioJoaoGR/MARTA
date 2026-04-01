
from pymonet.either import Either, Right, Left

def test_valid_input():
    # Test creating a Right instance
    right_value = Right(42)
    either_right = Either(right_value)
    assert isinstance(either_right, Either)
    assert either_right.is_right() is True

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

pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test creating a Right instance
        right_value = Right(42)
        either_right = Either(right_value)
        assert isinstance(either_right, Either)
>       assert either_right.is_right() is True
E       assert None is True
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7f419a4a81d0>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___0_test_valid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""
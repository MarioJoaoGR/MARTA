
import pytest
from pymonet.either import Either, Left, Right

def test_valid_input():
    # Test valid input with a Right value
    right_value = Either(Right("success"))
    assert isinstance(right_value, Either)
    assert right_value.to_box().value == "success"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test valid input with a Right value
        right_value = Either(Right("success"))
        assert isinstance(right_value, Either)
>       assert right_value.to_box().value == "success"
E       AssertionError: assert <pymonet.either.Right object at 0x7fb129df04d0> == 'success'
E        +  where <pymonet.either.Right object at 0x7fb129df04d0> = <pymonet.box.Box object at 0x7fb129d2dad0>.value
E        +    where <pymonet.box.Box object at 0x7fb129d2dad0> = to_box()
E        +      where to_box = <pymonet.either.Either object at 0x7fb12af75e50>.to_box

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_valid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""
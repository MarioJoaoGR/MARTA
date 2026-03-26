
import pytest
from pymonet.lazy import Lazy

@pytest.fixture(name="lazy")
def fixture_lazy():
    def square(x):
        return x * x
    return Lazy(square)

def test_valid_inputs(lazy):
    assert not lazy.is_evaluated
    result = lazy.fold()
    assert lazy.is_evaluated
    assert lazy.value == result

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

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_maybe_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

lazy = <pymonet.lazy.Lazy object at 0x7f5098a863d0>

    def test_valid_inputs(lazy):
        assert not lazy.is_evaluated
>       result = lazy.fold()
E       AttributeError: 'Lazy' object has no attribute 'fold'

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_maybe_0_test_valid_inputs.py:13: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_maybe_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.06s ===============================
"""
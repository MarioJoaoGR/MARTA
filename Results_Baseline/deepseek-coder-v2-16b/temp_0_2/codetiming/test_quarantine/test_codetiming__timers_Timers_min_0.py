
import pytest
from codetiming._timers import Timers
import collections

# Fixture to create an instance of Timers for each test
@pytest.fixture
def timers():
    return Timers()

def test_min_with_no_values(timers):
    """Test the min method with no values."""
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/codetiming
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

codetiming/Test4DT_tests/test_codetiming__timers_Timers_min_0.py F.      [100%]

=================================== FAILURES ===================================
___________________________ test_min_with_no_values ____________________________

timers = {}

    def test_min_with_no_values(timers):
        """Test the min method with no values."""
>       assert timers.min("operation1") == 0, f"Expected 0 but got {timers.min('operation1')}"

codetiming/Test4DT_tests/test_codetiming__timers_Timers_min_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
codetiming/codetiming/_timers.py:58: in min
    return self.apply(lambda values: min(values or [0]), name=name)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = {}, func = <function Timers.min.<locals>.<lambda> at 0x106837250>
name = 'operation1'

    def apply(self, func: Callable[[List[float]], float], name: str) -> float:
        """Apply a function to the results of one named timer."""
        if name in self._timings:
            return func(self._timings[name])
>       raise KeyError(name)
E       KeyError: 'operation1'

codetiming/codetiming/_timers.py:46: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timers_Timers_min_0.py::test_min_with_no_values
========================= 1 failed, 1 passed in 0.02s ==========================

"""

import pytest
from codetiming._timers import Timers

def test_none_value():
    timers = Timers()
    timers.add('task2', None)
    assert 'task2' in timers._timings
    assert timers._timings['task2'] == [None]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/codetiming
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_none_value.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_value ________________________________

    def test_none_value():
        timers = Timers()
>       timers.add('task2', None)

codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_none_value.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = {'task2': 0}, name = 'task2', value = None

    def add(self, name: str, value: float) -> None:
        """Add a timing value to the given timer."""
        self._timings[name].append(value)
        self.data.setdefault(name, 0)
>       self.data[name] += value
E       TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType'

codetiming/codetiming/_timers.py:28: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_none_value.py::test_none_value
============================== 1 failed in 0.02s ===============================
"""
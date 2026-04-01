
import pytest
from codetiming._timers import Timers

def test_edge_case():
    timers = Timers()
    
    # Test applying a function to a non-existent timer (should raise KeyError)
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), 'non_existent_timer')
    
    # Test applying a function to an empty list (should return 0 or appropriate result based on the function)
    assert timers.apply(lambda x: sum(x), 'empty_timer') == 0

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

codetiming/Test4DT_tests/test_codetiming__timers_Timers_apply_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        timers = Timers()
    
        # Test applying a function to a non-existent timer (should raise KeyError)
        with pytest.raises(KeyError):
            timers.apply(lambda x: sum(x), 'non_existent_timer')
    
        # Test applying a function to an empty list (should return 0 or appropriate result based on the function)
>       assert timers.apply(lambda x: sum(x), 'empty_timer') == 0

codetiming/Test4DT_tests/test_codetiming__timers_Timers_apply_0_test_edge_case.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = {}, func = <function test_edge_case.<locals>.<lambda> at 0x105e06710>
name = 'empty_timer'

    def apply(self, func: Callable[[List[float]], float], name: str) -> float:
        """Apply a function to the results of one named timer."""
        if name in self._timings:
            return func(self._timings[name])
>       raise KeyError(name)
E       KeyError: 'empty_timer'

codetiming/codetiming/_timers.py:46: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timers_Timers_apply_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.02s ===============================
"""
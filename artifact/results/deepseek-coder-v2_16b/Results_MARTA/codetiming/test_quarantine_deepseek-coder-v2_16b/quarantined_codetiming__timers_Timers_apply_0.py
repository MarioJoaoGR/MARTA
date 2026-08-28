
import pytest
from codetiming._timers import Timers
from typing import List, Callable

# Test for invalid input when applying a function to a timer
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/codetiming/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/codetiming/Test4DT_tests_deepseek-coder-v2_16b/test_codetiming__timers_Timers_apply_0.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_apply ___________________________

    def test_invalid_input_apply():
        timers = Timers()
        func = None
        name = None
    
        with pytest.raises(TypeError):
>           timers.apply(func, name)

/opt/marta/baselines/Results_MARTA/codetiming/Test4DT_tests_deepseek-coder-v2_16b/test_codetiming__timers_Timers_apply_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = {}, func = None, name = None

    def apply(self, func: Callable[[List[float]], float], name: str) -> float:
        """Apply a function to the results of one named timer"""
        if name in self._timings:
            return func(self._timings[name])
>       raise KeyError(name)
E       KeyError: None

/opt/marta/baselines/codamosa/replication/test-apps/codetiming/codetiming/_timers.py:46: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/codetiming/Test4DT_tests_deepseek-coder-v2_16b/test_codetiming__timers_Timers_apply_0.py::test_invalid_input_apply
============================== 1 failed in 0.06s ===============================
"""
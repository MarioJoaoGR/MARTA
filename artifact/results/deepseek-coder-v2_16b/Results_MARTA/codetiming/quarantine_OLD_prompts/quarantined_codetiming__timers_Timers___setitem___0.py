
import pytest
from codetiming import Timers
import statistics
import math

def test_stdev_timing():
    timers = Timers()
    timers.add('task5', 1.23)
    timers.add('task5', 4.56)
    assert timers.stdev('task5') == pytest.approx(math.sqrt(((1.23 - (1.23 + 4.56) / 2) ** 2 + (4.56 - (1.23 + 4.56) / 2) ** 2) / 2), abs=0.01)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/codetiming/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting test_codetiming__timers_Timers___setitem___0.py _______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/codetiming/Test4DT_tests_deepseek-coder-v2_16b/test_codetiming__timers_Timers___setitem___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/codetiming/Test4DT_tests_deepseek-coder-v2_16b/test_codetiming__timers_Timers___setitem___0.py:3: in <module>
    from codetiming import Timers
E   ImportError: cannot import name 'Timers' from 'codetiming' (/opt/marta/baselines/codamosa/replication/test-apps/codetiming/codetiming/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/codetiming/Test4DT_tests_deepseek-coder-v2_16b/test_codetiming__timers_Timers___setitem___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""

import pytest
from flutes.log import log, LoggingLevel, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, COLOR_MAP, LOGGING_MAP, LOGGER, get_worker_id, colored, _CONSOLE_LOG_FN

def test_edge_cases():
    with pytest.raises(ValueError):
        log(None)  # Test None input for msg

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_log_0_test_edge_cases.py F          [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_log_log_0_test_edge_cases.py:6: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-24 16:17:01] None
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 None
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_log_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.09s ===============================
"""
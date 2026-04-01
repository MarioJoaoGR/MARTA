
import pytest
from flutes.log import log, LoggingLevel, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, COLOR_MAP, LOGGING_MAP, LOGGER
from unittest.mock import patch

def test_edge_cases():
    with pytest.raises(ValueError):
        # Test None input for msg
        log(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_log_0_test_edge_cases.py F          [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_log_log_0_test_edge_cases.py:7: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-22 19:16:36] None
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 None
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_log_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.10s ===============================
"""
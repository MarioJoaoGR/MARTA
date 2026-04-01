
import pytest
from flutes.log import log, LOGGING_MAP, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, COLOR_MAP, LOGGER, LOGGING_MAP
from unittest.mock import patch

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test with an invalid logging level
        log("Test message", level="invalid_level")
        
    with pytest.raises(ValueError):
        # Test with a non-string message
        log(12345, level="info")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_log_4_test_invalid_inputs.py F      [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError):
            # Test with an invalid logging level
            log("Test message", level="invalid_level")
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_log_log_4_test_invalid_inputs.py:11: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-22 20:22:38] 12345
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 12345
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_log_4_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.12s ===============================
"""
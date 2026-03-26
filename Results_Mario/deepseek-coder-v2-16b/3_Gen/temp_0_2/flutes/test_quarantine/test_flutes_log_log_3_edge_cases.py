
import pytest
from flutes.log import log, LOGGING_MAP, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, COLOR_MAP, LOGGER
from unittest.mock import patch

def test_log_edge_cases():
    with pytest.raises(ValueError):
        # Test with an incorrect logging level
        log("Test message", level="invalid_level")
    
    with pytest.raises(TypeError):
        # Test with a non-string message
        log(None, level="info")
    
    with patch('flutes.log._CONSOLE_LOG_FN') as mock_console_log:
        # Test without timestamp and include_proc_id set to False
        log("Test message", force_console=True)
        assert not mock_console_log.called
    
    with patch('flutes.log._CONSOLE_LOG_FN') as mock_console_log:
        # Test without timestamp and include_proc_id set to True
        log("Test message", force_console=True, include_proc_id=False)
        assert not mock_console_log.called
    
    with patch('flutes.log._CONSOLE_LOG_FN') as mock_console_log:
        # Test with timestamp and include_proc_id set to False
        log("Test message", force_console=True, timestamp=False)
        assert not mock_console_log.called
    
    with patch('flutes.log._CONSOLE_LOG_FN') as mock_console_log:
        # Test with timestamp and include_proc_id set to True
        log("Test message", force_console=True, timestamp=True, include_proc_id=True)
        assert mock_console_log.called
    
    with patch('flutes.log._CONSOLE_LOG_FN') as mock_console_log:
        # Test without force_console and default settings
        log("Test message")
        assert not mock_console_log.called

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

flutes/Test4DT_tests/test_flutes_log_log_3_edge_cases.py F               [100%]

=================================== FAILURES ===================================
_____________________________ test_log_edge_cases ______________________________

    def test_log_edge_cases():
        with pytest.raises(ValueError):
            # Test with an incorrect logging level
            log("Test message", level="invalid_level")
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_log_log_3_edge_cases.py:11: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-24 00:42:21] None
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 None
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_log_3_edge_cases.py::test_log_edge_cases
============================== 1 failed in 0.11s ===============================
"""
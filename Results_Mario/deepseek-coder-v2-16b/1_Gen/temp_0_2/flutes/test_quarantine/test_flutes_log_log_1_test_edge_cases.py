
import pytest
from flutes.log import log, LEVEL_MAP, _CONSOLE_LOG_FN, LOGGING_MAP
from unittest.mock import patch

@pytest.fixture(autouse=True)
def setup():
    LEVEL_MAP["info"] = 20
    yield
    LEVEL_MAP.pop("info")

def test_log_info():
    captured = []
    
    def mock_console_log(msg):
        captured.append(msg)
    
    with patch('flutes.log._CONSOLE_LOG_FN', new=mock_console_log):
        log("Test info message", level="info")
        
        assert len(captured) == 1, "Expected one logged message"
        assert captured[0] == "Test info message", "Unexpected message content"

def test_log_error():
    captured = []
    
    def mock_console_log(msg):
        captured.append(msg)
    
    with patch('flutes.log._CONSOLE_LOG_FN', new=mock_console_log):
        LEVEL_MAP["error"] = 40
        log("Test error message", level="error")
        
        assert len(captured) == 1, "Expected one logged message"
        assert captured[0] == "Test error message", "Unexpected message content"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_log_log_1_test_edge_cases.py FF         [100%]

=================================== FAILURES ===================================
________________________________ test_log_info _________________________________

    def test_log_info():
        captured = []
    
        def mock_console_log(msg):
            captured.append(msg)
    
        with patch('flutes.log._CONSOLE_LOG_FN', new=mock_console_log):
            log("Test info message", level="info")
    
            assert len(captured) == 1, "Expected one logged message"
>           assert captured[0] == "Test info message", "Unexpected message content"
E           AssertionError: Unexpected message content
E           assert '[2026-03-24 ... info message' == 'Test info message'
E             
E             - Test info message
E             + [2026-03-24 18:27:33] Test info message

flutes/Test4DT_tests/test_flutes_log_log_1_test_edge_cases.py:22: AssertionError
------------------------------ Captured log call -------------------------------
INFO     flutes.log:log.py:182 Test info message
________________________________ test_log_error ________________________________

    def test_log_error():
        captured = []
    
        def mock_console_log(msg):
            captured.append(msg)
    
        with patch('flutes.log._CONSOLE_LOG_FN', new=mock_console_log):
            LEVEL_MAP["error"] = 40
            log("Test error message", level="error")
    
            assert len(captured) == 1, "Expected one logged message"
>           assert captured[0] == "Test error message", "Unexpected message content"
E           AssertionError: Unexpected message content
E           assert '[2026-03-24 ...error message' == 'Test error message'
E             
E             - Test error message
E             + [2026-03-24 18:27:33] Test error message

flutes/Test4DT_tests/test_flutes_log_log_1_test_edge_cases.py:35: AssertionError
------------------------------ Captured log call -------------------------------
ERROR    flutes.log:log.py:182 Test error message
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_log_1_test_edge_cases.py::test_log_info
FAILED flutes/Test4DT_tests/test_flutes_log_log_1_test_edge_cases.py::test_log_error
============================== 2 failed in 0.09s ===============================
"""
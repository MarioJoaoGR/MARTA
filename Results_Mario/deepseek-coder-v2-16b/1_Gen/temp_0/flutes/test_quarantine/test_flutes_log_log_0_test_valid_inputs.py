
import pytest
from unittest.mock import patch, MagicMock
from flutes.log import log  # Assuming 'flutes.log' is the correct module path

# Mocking necessary functions and constants if used in the function
@patch('flutes.log._CONSOLE_LOG_FN', create=True)
@patch('flutes.log.time')
@patch('flutes.log.colored')
@patch('flutes.log.get_worker_id', return_value="mocked_worker_id")
def test_valid_inputs(mock_get_worker_id, mock_colored, mock_time, mock_console_log):
    # Test cases for different inputs and configurations
    
    with patch('flutes.log._CONSOLE_LOG_FN') as mocked_console_log:
        log("Test message", level="info")
        assert "Test message" in str(mocked_console_log.call_args)
        
        # Add more test cases for different levels, force_console, timestamp, and include_proc_id settings

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

flutes/Test4DT_tests/test_flutes_log_log_0_test_valid_inputs.py F        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

mock_get_worker_id = <MagicMock name='get_worker_id' id='140686762106320'>
mock_colored = <MagicMock name='colored' id='140686762112080'>
mock_time = <MagicMock name='time' id='140686762001168'>
mock_console_log = <MagicMock name='_CONSOLE_LOG_FN' id='140686762009040'>

    @patch('flutes.log._CONSOLE_LOG_FN', create=True)
    @patch('flutes.log.time')
    @patch('flutes.log.colored')
    @patch('flutes.log.get_worker_id', return_value="mocked_worker_id")
    def test_valid_inputs(mock_get_worker_id, mock_colored, mock_time, mock_console_log):
        # Test cases for different inputs and configurations
    
        with patch('flutes.log._CONSOLE_LOG_FN') as mocked_console_log:
>           log("Test message", level="info")

flutes/Test4DT_tests/test_flutes_log_log_0_test_valid_inputs.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

msg = 'Test message', level = 'info', force_console = False, timestamp = True
include_proc_id = True

    def log(msg: str, level: LoggingLevel = "info", force_console: bool = False,
            timestamp: bool = True, include_proc_id: bool = True) -> None:
        r"""Write a line of log with the specified logging level.
    
        :param msg: Message to log.
        :param level: Logging level. Available options are ``success``, ``warning``, ``error``, and ``info``. Defaults to
            ``info``.
        :param force_console: If ``True``, will write to console regardless of logging level setting. Defaults to ``False``.
        :param timestamp: If ``True``, will add a timestamp to the console logging output. Defaults to ``True``.
    
            ..note::
                The logging level colors apply to the timestamp only, so if :attr:`timestamp` is set to ``False``, then
                it's not possible to differentiate between different logging levels under console.
    
        :param include_proc_id: If ``True``, will include the process ID for multiprocessing pool workers. Defaults to
            ``True``.
        """
        if level not in LOGGING_MAP:
            raise ValueError(f"Incorrect logging level '{level}'")
        msg = str(msg)
        if include_proc_id:
            worker_id = get_worker_id()
            if worker_id is not None:
>               msg = f"(Worker {worker_id:2d}) {msg}"
E               ValueError: Unknown format code 'd' for object of type 'str'

flutes/flutes/log.py:174: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_log_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.09s ===============================
"""
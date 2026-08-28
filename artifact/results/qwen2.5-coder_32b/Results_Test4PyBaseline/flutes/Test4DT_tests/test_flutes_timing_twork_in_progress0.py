
import pytest
from unittest.mock import patch, call  # Import 'call' from unittest.mock
from flutes.timing import work_in_progress

def test_work_in_progress_decorator():
    @work_in_progress("Test task")
    def dummy_function():
        pass

    with patch('builtins.print') as mock_print:
        dummy_function()
        mock_print.assert_has_calls([
            call("Test task... ", end='', flush=True),
            call("done. (0.00s)")
        ])

def test_work_in_progress_context_manager():
    with patch('builtins.print') as mock_print:
        with work_in_progress("Another test"):
            pass
        mock_print.assert_has_calls([
            call("Another test... ", end='', flush=True),
            call("done. (0.00s)")
        ])

def test_work_in_progress_default_description():
    @work_in_progress()
    def default_desc_function():
        pass

    with patch('builtins.print') as mock_print:
        default_desc_function()
        mock_print.assert_has_calls([
            call("Work in progress... ", end='', flush=True),
            call("done. (0.00s)")
        ])

def test_work_in_progress_with_delay():
    import time

    @work_in_progress("Delayed task")
    def delayed_function():
        time.sleep(0.1)

    with patch('builtins.print') as mock_print:
        delayed_function()
        mock_print.assert_has_calls([
            call("Delayed task... ", end='', flush=True),
            call("done. (0.10s)")
        ])

def test_work_in_progress_context_manager_with_delay():
    import time

    with patch('builtins.print') as mock_print:
        with work_in_progress("Context manager delay"):
            time.sleep(0.1)
        mock_print.assert_has_calls([
            call("Context manager delay... ", end='', flush=True),
            call("done. (0.10s)")
        ])

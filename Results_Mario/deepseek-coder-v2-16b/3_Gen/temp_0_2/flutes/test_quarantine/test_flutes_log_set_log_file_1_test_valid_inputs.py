
import pytest
from unittest.mock import patch, call
from pathlib import Path
from flutes.log import set_log_file, _remove_handlers, MultiprocessingFileHandler, LOGGER

@pytest.mark.parametrize("fmt", [
    "%(asctime)s %(levelname)s: %(message)s",
    "%Y-%m-%d %H:%M:%S - %(levelname)s - %(message)s"
])
def test_valid_inputs(fmt):
    with patch('flutes.log._remove_handlers') as mock_remove_handlers, \
         patch('logging.getLogger') as mock_get_logger, \
         patch('flutes.log.MultiprocessingFileHandler') as mock_multiprocessing_handler:

        # Mock the logger and its handlers
        mock_logger = mock_get_logger.return_value
        mock_handler = mock_multiprocessing_handler.return_value

        # Call the function with a valid path and format
        set_log_file(Path('logs/application.log'), fmt=fmt)

        # Assert that _remove_handlers was called once with the mock logger
        mock_remove_handlers.assert_called_once_with(mock_logger)

        # Assert that MultiprocessingFileHandler was called once with the correct arguments
        expected_calls = [call(Path('logs/application.log'), mode="a")]
        assert mock_multiprocessing_handler.call_args_list == expected_calls

        # Assert that the logger has a handler of type MultiprocessingFileHandler
        assert len(mock_logger.handlers) == 1
        assert isinstance(mock_logger.handlers[0], MultiprocessingFileHandler)

        # Assert that the formatter is set correctly
        for handler in mock_logger.handlers:
            if isinstance(handler, MultiprocessingFileHandler):
                assert handler.formatter._fmt == fmt

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

flutes/Test4DT_tests/test_flutes_log_set_log_file_1_test_valid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________ test_valid_inputs[%(asctime)s %(levelname)s: %(message)s] ___________

fmt = '%(asctime)s %(levelname)s: %(message)s'

    @pytest.mark.parametrize("fmt", [
        "%(asctime)s %(levelname)s: %(message)s",
        "%Y-%m-%d %H:%M:%S - %(levelname)s - %(message)s"
    ])
    def test_valid_inputs(fmt):
        with patch('flutes.log._remove_handlers') as mock_remove_handlers, \
             patch('logging.getLogger') as mock_get_logger, \
             patch('flutes.log.MultiprocessingFileHandler') as mock_multiprocessing_handler:
    
            # Mock the logger and its handlers
            mock_logger = mock_get_logger.return_value
            mock_handler = mock_multiprocessing_handler.return_value
    
            # Call the function with a valid path and format
            set_log_file(Path('logs/application.log'), fmt=fmt)
    
            # Assert that _remove_handlers was called once with the mock logger
>           mock_remove_handlers.assert_called_once_with(mock_logger)

flutes/Test4DT_tests/test_flutes_log_set_log_file_1_test_valid_inputs.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:951: in assert_called_once_with
    return self.assert_called_with(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='_remove_handlers' id='139774758205776'>
args = (<MagicMock name='getLogger()' id='139774744530960'>,), kwargs = {}
expected = call(<MagicMock name='getLogger()' id='139774744530960'>)
actual = call(<Logger flutes.log (INFO)>)
_error_message = <function NonCallableMock.assert_called_with.<locals>._error_message at 0x7f1fd7fa4e00>
cause = None

    def assert_called_with(self, /, *args, **kwargs):
        """assert that the last call was made with the specified arguments.
    
        Raises an AssertionError if the args and keyword args passed in are
        different to the last call to the mock."""
        if self.call_args is None:
            expected = self._format_mock_call_signature(args, kwargs)
            actual = 'not called.'
            error_message = ('expected call not found.\nExpected: %s\n  Actual: %s'
                    % (expected, actual))
            raise AssertionError(error_message)
    
        def _error_message():
            msg = self._format_mock_failure_message(args, kwargs)
            return msg
        expected = self._call_matcher(_Call((args, kwargs), two=True))
        actual = self._call_matcher(self.call_args)
        if actual != expected:
            cause = expected if isinstance(expected, Exception) else None
>           raise AssertionError(_error_message()) from cause
E           AssertionError: expected call not found.
E           Expected: _remove_handlers(<MagicMock name='getLogger()' id='139774744530960'>)
E             Actual: _remove_handlers(<Logger flutes.log (INFO)>)

/usr/local/lib/python3.11/unittest/mock.py:939: AssertionError
______ test_valid_inputs[%Y-%m-%d %H:%M:%S - %(levelname)s - %(message)s] ______

fmt = '%Y-%m-%d %H:%M:%S - %(levelname)s - %(message)s'

    @pytest.mark.parametrize("fmt", [
        "%(asctime)s %(levelname)s: %(message)s",
        "%Y-%m-%d %H:%M:%S - %(levelname)s - %(message)s"
    ])
    def test_valid_inputs(fmt):
        with patch('flutes.log._remove_handlers') as mock_remove_handlers, \
             patch('logging.getLogger') as mock_get_logger, \
             patch('flutes.log.MultiprocessingFileHandler') as mock_multiprocessing_handler:
    
            # Mock the logger and its handlers
            mock_logger = mock_get_logger.return_value
            mock_handler = mock_multiprocessing_handler.return_value
    
            # Call the function with a valid path and format
            set_log_file(Path('logs/application.log'), fmt=fmt)
    
            # Assert that _remove_handlers was called once with the mock logger
>           mock_remove_handlers.assert_called_once_with(mock_logger)

flutes/Test4DT_tests/test_flutes_log_set_log_file_1_test_valid_inputs.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:951: in assert_called_once_with
    return self.assert_called_with(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='_remove_handlers' id='139774742287504'>
args = (<MagicMock name='getLogger()' id='139774744036880'>,), kwargs = {}
expected = call(<MagicMock name='getLogger()' id='139774744036880'>)
actual = call(<Logger flutes.log (INFO)>)
_error_message = <function NonCallableMock.assert_called_with.<locals>._error_message at 0x7f1fd7fa54e0>
cause = None

    def assert_called_with(self, /, *args, **kwargs):
        """assert that the last call was made with the specified arguments.
    
        Raises an AssertionError if the args and keyword args passed in are
        different to the last call to the mock."""
        if self.call_args is None:
            expected = self._format_mock_call_signature(args, kwargs)
            actual = 'not called.'
            error_message = ('expected call not found.\nExpected: %s\n  Actual: %s'
                    % (expected, actual))
            raise AssertionError(error_message)
    
        def _error_message():
            msg = self._format_mock_failure_message(args, kwargs)
            return msg
        expected = self._call_matcher(_Call((args, kwargs), two=True))
        actual = self._call_matcher(self.call_args)
        if actual != expected:
            cause = expected if isinstance(expected, Exception) else None
>           raise AssertionError(_error_message()) from cause
E           AssertionError: expected call not found.
E           Expected: _remove_handlers(<MagicMock name='getLogger()' id='139774744036880'>)
E             Actual: _remove_handlers(<Logger flutes.log (INFO)>)

/usr/local/lib/python3.11/unittest/mock.py:939: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_log_file_1_test_valid_inputs.py::test_valid_inputs[%(asctime)s %(levelname)s: %(message)s]
FAILED flutes/Test4DT_tests/test_flutes_log_set_log_file_1_test_valid_inputs.py::test_valid_inputs[%Y-%m-%d %H:%M:%S - %(levelname)s - %(message)s]
============================== 2 failed in 0.20s ===============================
"""
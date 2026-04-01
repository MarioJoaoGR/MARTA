
import pytest
from isort.format import show_unified_diff, create_terminal_printer
from pathlib import Path
from io import StringIO
from datetime import datetime
import os
import sys
from unittest.mock import patch

@pytest.mark.parametrize("color_output, expected", [(True, "colored"), (False, "plain")])
def test_show_unified_diff(color_output, expected):
    file_input = "old content"
    file_output = "new content"
    file_path = Path("example/path/to/file.txt")
    output = StringIO()
    
    with patch('sys.stderr') as mock_stderr:
        with pytest.raises(SystemExit) as excinfo:
            show_unified_diff(file_input=file_input, file_output=file_output, file_path=file_path, output=output, color_output=color_output)
        
        assert excinfo.type == SystemExit
        mock_stderr.write.assert_called_with("\nSorry, but to use --color (color_output) the colorama python package is required.\n\nReference: https://pypi.org/project/colorama/\n\nYou can either install it separately on your system or as the colors extra for isort. Ex: \n\n$ pip install isort[colors]\n")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_valid_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________ test_show_unified_diff[True-colored] _____________________

color_output = True, expected = 'colored'

    @pytest.mark.parametrize("color_output, expected", [(True, "colored"), (False, "plain")])
    def test_show_unified_diff(color_output, expected):
        file_input = "old content"
        file_output = "new content"
        file_path = Path("example/path/to/file.txt")
        output = StringIO()
    
        with patch('sys.stderr') as mock_stderr:
            with pytest.raises(SystemExit) as excinfo:
                show_unified_diff(file_input=file_input, file_output=file_output, file_path=file_path, output=output, color_output=color_output)
    
            assert excinfo.type == SystemExit
>           mock_stderr.write.assert_called_with("\nSorry, but to use --color (color_output) the colorama python package is required.\n\nReference: https://pypi.org/project/colorama/\n\nYou can either install it separately on your system or as the colors extra for isort. Ex: \n\n$ pip install isort[colors]\n")

isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_valid_case.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='stderr.write' id='140693425017488'>
args = ('\nSorry, but to use --color (color_output) the colorama python package is required.\n\nReference: https://pypi.org/p... either install it separately on your system or as the colors extra for isort. Ex: \n\n$ pip install isort[colors]\n',)
kwargs = {}
expected = call('\nSorry, but to use --color (color_output) the colorama python package is required.\n\nReference: https://pypi.o...n either install it separately on your system or as the colors extra for isort. Ex: \n\n$ pip install isort[colors]\n')
actual = call('\n')
_error_message = <function NonCallableMock.assert_called_with.<locals>._error_message at 0x7ff5bd9f8040>
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
E           Expected: write('\nSorry, but to use --color (color_output) the colorama python package is required.\n\nReference: https://pypi.org/project/colorama/\n\nYou can either install it separately on your system or as the colors extra for isort. Ex: \n\n$ pip install isort[colors]\n')
E             Actual: write('\n')

/usr/local/lib/python3.11/unittest/mock.py:939: AssertionError
_____________________ test_show_unified_diff[False-plain] ______________________

color_output = False, expected = 'plain'

    @pytest.mark.parametrize("color_output, expected", [(True, "colored"), (False, "plain")])
    def test_show_unified_diff(color_output, expected):
        file_input = "old content"
        file_output = "new content"
        file_path = Path("example/path/to/file.txt")
        output = StringIO()
    
        with patch('sys.stderr') as mock_stderr:
            with pytest.raises(SystemExit) as excinfo:
>               show_unified_diff(file_input=file_input, file_output=file_output, file_path=file_path, output=output, color_output=color_output)

isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_valid_case.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/format.py:62: in show_unified_diff
    datetime.now() if file_path is None else datetime.fromtimestamp(file_path.stat().st_mtime)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = PosixPath('example/path/to/file.txt')

    def stat(self, *, follow_symlinks=True):
        """
        Return the result of the stat() system call on this path, like
        os.stat() does.
        """
>       return os.stat(self, follow_symlinks=follow_symlinks)
E       FileNotFoundError: [Errno 2] No such file or directory: 'example/path/to/file.txt'

/usr/local/lib/python3.11/pathlib.py:1013: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_valid_case.py::test_show_unified_diff[True-colored]
FAILED isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_valid_case.py::test_show_unified_diff[False-plain]
============================== 2 failed in 0.17s ===============================
"""
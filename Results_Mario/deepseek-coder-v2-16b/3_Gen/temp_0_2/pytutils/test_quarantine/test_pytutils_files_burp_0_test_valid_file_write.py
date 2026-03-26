
import pytest
import os
import sys
from pytutils.files import burp

@pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars, expected", [
    ('example.txt', 'Hello, world!', 'w', True, True, True, None),
    ('-', 'Hello, world!', 'w', True, False, False, None),
    ('~/documents/report.txt', 'Report data', 'w', True, True, True, None)
])
def test_valid_file_write(filename, contents, mode, allow_stdout, expanduser, expandvars, expected):
    if filename == '-':
        with pytest.raises(SystemExit):  # Assuming burp will exit when writing to stdout is not allowed
            burp(filename, contents, mode=mode, allow_stdout=allow_stdout, expanduser=expanduser, expandvars=expandvars)
    else:
        if expanduser or expandvars:
            expected_expanded = os.path.expanduser(os.path.expandvars(filename))
        else:
            expected_expanded = filename

        with pytest.raises(SystemExit):  # Assuming burp will exit when writing to stdout is not allowed
            burp(filename, contents, mode=mode, allow_stdout=allow_stdout, expanduser=expanduser, expandvars=expandvars)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_file_write.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____ test_valid_file_write[example.txt-Hello, world!-w-True-True-True-None] ____

filename = 'example.txt', contents = 'Hello, world!', mode = 'w'
allow_stdout = True, expanduser = True, expandvars = True, expected = None

    @pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars, expected", [
        ('example.txt', 'Hello, world!', 'w', True, True, True, None),
        ('-', 'Hello, world!', 'w', True, False, False, None),
        ('~/documents/report.txt', 'Report data', 'w', True, True, True, None)
    ])
    def test_valid_file_write(filename, contents, mode, allow_stdout, expanduser, expandvars, expected):
        if filename == '-':
            with pytest.raises(SystemExit):  # Assuming burp will exit when writing to stdout is not allowed
                burp(filename, contents, mode=mode, allow_stdout=allow_stdout, expanduser=expanduser, expandvars=expandvars)
        else:
            if expanduser or expandvars:
                expected_expanded = os.path.expanduser(os.path.expandvars(filename))
            else:
                expected_expanded = filename
    
>           with pytest.raises(SystemExit):  # Assuming burp will exit when writing to stdout is not allowed
E           Failed: DID NOT RAISE <class 'SystemExit'>

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_file_write.py:22: Failed
________ test_valid_file_write[--Hello, world!-w-True-False-False-None] ________

filename = '-', contents = 'Hello, world!', mode = 'w', allow_stdout = True
expanduser = False, expandvars = False, expected = None

    @pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars, expected", [
        ('example.txt', 'Hello, world!', 'w', True, True, True, None),
        ('-', 'Hello, world!', 'w', True, False, False, None),
        ('~/documents/report.txt', 'Report data', 'w', True, True, True, None)
    ])
    def test_valid_file_write(filename, contents, mode, allow_stdout, expanduser, expandvars, expected):
        if filename == '-':
>           with pytest.raises(SystemExit):  # Assuming burp will exit when writing to stdout is not allowed
E           Failed: DID NOT RAISE <class 'SystemExit'>

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_file_write.py:14: Failed
----------------------------- Captured stdout call -----------------------------
Hello, world!
_ test_valid_file_write[~/documents/report.txt-Report data-w-True-True-True-None] _

filename = '~/documents/report.txt', contents = 'Report data', mode = 'w'
allow_stdout = True, expanduser = True, expandvars = True, expected = None

    @pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars, expected", [
        ('example.txt', 'Hello, world!', 'w', True, True, True, None),
        ('-', 'Hello, world!', 'w', True, False, False, None),
        ('~/documents/report.txt', 'Report data', 'w', True, True, True, None)
    ])
    def test_valid_file_write(filename, contents, mode, allow_stdout, expanduser, expandvars, expected):
        if filename == '-':
            with pytest.raises(SystemExit):  # Assuming burp will exit when writing to stdout is not allowed
                burp(filename, contents, mode=mode, allow_stdout=allow_stdout, expanduser=expanduser, expandvars=expandvars)
        else:
            if expanduser or expandvars:
                expected_expanded = os.path.expanduser(os.path.expandvars(filename))
            else:
                expected_expanded = filename
    
            with pytest.raises(SystemExit):  # Assuming burp will exit when writing to stdout is not allowed
>               burp(filename, contents, mode=mode, allow_stdout=allow_stdout, expanduser=expanduser, expandvars=expandvars)

pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_file_write.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = '/home/joaovitorino/documents/report.txt', contents = 'Report data'
mode = 'w', allow_stdout = True, expanduser = True, expandvars = True

    def burp(filename, contents, mode='w', allow_stdout=True, expanduser=True, expandvars=True):
        """
        Write `contents` to `filename`.
        """
        if filename == '-' and allow_stdout:
            sys.stdout.write(contents)
        else:
            if expanduser:
                filename = os.path.expanduser(filename)
            if expandvars:
                filename = os.path.expandvars(filename)
    
>           with open(filename, mode) as fh:
E           FileNotFoundError: [Errno 2] No such file or directory: '/home/joaovitorino/documents/report.txt'

pytutils/pytutils/files.py:67: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_file_write.py::test_valid_file_write[example.txt-Hello, world!-w-True-True-True-None]
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_file_write.py::test_valid_file_write[--Hello, world!-w-True-False-False-None]
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_0_test_valid_file_write.py::test_valid_file_write[~/documents/report.txt-Report data-w-True-True-True-None]
============================== 3 failed in 0.06s ===============================
"""
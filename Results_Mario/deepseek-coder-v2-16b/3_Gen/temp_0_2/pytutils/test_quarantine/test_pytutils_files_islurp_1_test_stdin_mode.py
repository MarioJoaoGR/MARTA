
import pytest
import sys
import os
import functools
from pytutils.files import islurp

LINEMODE = 100  # Assuming LINEMODE is defined somewhere in the module

@pytest.mark.parametrize("filename, mode, iter_by, allow_stdin, expanduser, expandvars", [
    ('-', 'r', LINEMODE, True, True, True),  # Test reading from stdin
    ('example.txt', 'r', LINEMODE, False, True, True),  # Test reading a local file
    ('~/example.txt', 'r', LINEMODE, False, True, True),  # Test expanding user home directory in filename
    ('$HOME/example.txt', 'r', LINEMODE, False, True, True)  # Test expanding environment variables in filename
])
def test_stdin_mode(filename, mode, iter_by, allow_stdin, expanduser, expandvars):
    if filename == '-':
        with pytest.raises(TypeError):
            for line in islurp('-', mode=mode, iter_by=iter_by, allow_stdin=allow_stdin, expanduser=expanduser, expandvars=expandvars):
                print(line)
    else:
        # Mock sys.stdin to simulate stdin input if needed
        with pytest.raises(TypeError):
            for line in islurp(filename, mode=mode, iter_by=iter_by, allow_stdin=allow_stdin, expanduser=expanduser, expandvars=expandvars):
                print(line)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

pytutils/Test4DT_tests/test_pytutils_files_islurp_1_test_stdin_mode.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
___________________ test_stdin_mode[--r-100-True-True-True] ____________________

filename = '-', mode = 'r', iter_by = 100, allow_stdin = True, expanduser = True
expandvars = True

    @pytest.mark.parametrize("filename, mode, iter_by, allow_stdin, expanduser, expandvars", [
        ('-', 'r', LINEMODE, True, True, True),  # Test reading from stdin
        ('example.txt', 'r', LINEMODE, False, True, True),  # Test reading a local file
        ('~/example.txt', 'r', LINEMODE, False, True, True),  # Test expanding user home directory in filename
        ('$HOME/example.txt', 'r', LINEMODE, False, True, True)  # Test expanding environment variables in filename
    ])
    def test_stdin_mode(filename, mode, iter_by, allow_stdin, expanduser, expandvars):
        if filename == '-':
            with pytest.raises(TypeError):
>               for line in islurp('-', mode=mode, iter_by=iter_by, allow_stdin=allow_stdin, expanduser=expanduser, expandvars=expandvars):

pytutils/Test4DT_tests/test_pytutils_files_islurp_1_test_stdin_mode.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = '-', mode = 'r', iter_by = 100, allow_stdin = True, expanduser = True
expandvars = True

    def islurp(filename, mode='r', iter_by=LINEMODE, allow_stdin=True, expanduser=True, expandvars=True):
        """
        Read [expanded] `filename` and yield each (line | chunk).
    
        :param str filename: File path
        :param str mode: Use this mode to open `filename`, ala `r` for text (default), `rb` for binary, etc.
        :param int iter_by: Iterate by this many bytes at a time. Default is by line.
        :param bool allow_stdin: If Truthy and filename is `-`, read from `sys.stdin`.
        :param bool expanduser: If Truthy, expand `~` in `filename`
        :param bool expandvars: If Truthy, expand env vars in `filename`
        """
        if iter_by == 'LINEMODE':
            iter_by = LINEMODE
    
        fh = None
        try:
            if filename == '-' and allow_stdin:
                fh = sys.stdin
            else:
                if expanduser:
                    filename = os.path.expanduser(filename)
                if expandvars:
                    filename = os.path.expandvars(filename)
    
                fh = open(filename, mode)
                fh_next = fh.readline if iter_by == LINEMODE else functools.partial(fh.read, iter_by)
    
            while True:
>               buf = fh_next()
E               UnboundLocalError: cannot access local variable 'fh_next' where it is not associated with a value

pytutils/pytutils/files.py:40: UnboundLocalError
______________ test_stdin_mode[example.txt-r-100-False-True-True] ______________

filename = 'example.txt', mode = 'r', iter_by = 100, allow_stdin = False
expanduser = True, expandvars = True

    @pytest.mark.parametrize("filename, mode, iter_by, allow_stdin, expanduser, expandvars", [
        ('-', 'r', LINEMODE, True, True, True),  # Test reading from stdin
        ('example.txt', 'r', LINEMODE, False, True, True),  # Test reading a local file
        ('~/example.txt', 'r', LINEMODE, False, True, True),  # Test expanding user home directory in filename
        ('$HOME/example.txt', 'r', LINEMODE, False, True, True)  # Test expanding environment variables in filename
    ])
    def test_stdin_mode(filename, mode, iter_by, allow_stdin, expanduser, expandvars):
        if filename == '-':
            with pytest.raises(TypeError):
                for line in islurp('-', mode=mode, iter_by=iter_by, allow_stdin=allow_stdin, expanduser=expanduser, expandvars=expandvars):
                    print(line)
        else:
            # Mock sys.stdin to simulate stdin input if needed
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_islurp_1_test_stdin_mode.py:23: Failed
----------------------------- Captured stdout call -----------------------------
Hello, world!
_____________ test_stdin_mode[~/example.txt-r-100-False-True-True] _____________

filename = '~/example.txt', mode = 'r', iter_by = 100, allow_stdin = False
expanduser = True, expandvars = True

    @pytest.mark.parametrize("filename, mode, iter_by, allow_stdin, expanduser, expandvars", [
        ('-', 'r', LINEMODE, True, True, True),  # Test reading from stdin
        ('example.txt', 'r', LINEMODE, False, True, True),  # Test reading a local file
        ('~/example.txt', 'r', LINEMODE, False, True, True),  # Test expanding user home directory in filename
        ('$HOME/example.txt', 'r', LINEMODE, False, True, True)  # Test expanding environment variables in filename
    ])
    def test_stdin_mode(filename, mode, iter_by, allow_stdin, expanduser, expandvars):
        if filename == '-':
            with pytest.raises(TypeError):
                for line in islurp('-', mode=mode, iter_by=iter_by, allow_stdin=allow_stdin, expanduser=expanduser, expandvars=expandvars):
                    print(line)
        else:
            # Mock sys.stdin to simulate stdin input if needed
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_islurp_1_test_stdin_mode.py:23: Failed
----------------------------- Captured stdout call -----------------------------
Hello, world!
___________ test_stdin_mode[$HOME/example.txt-r-100-False-True-True] ___________

filename = '$HOME/example.txt', mode = 'r', iter_by = 100, allow_stdin = False
expanduser = True, expandvars = True

    @pytest.mark.parametrize("filename, mode, iter_by, allow_stdin, expanduser, expandvars", [
        ('-', 'r', LINEMODE, True, True, True),  # Test reading from stdin
        ('example.txt', 'r', LINEMODE, False, True, True),  # Test reading a local file
        ('~/example.txt', 'r', LINEMODE, False, True, True),  # Test expanding user home directory in filename
        ('$HOME/example.txt', 'r', LINEMODE, False, True, True)  # Test expanding environment variables in filename
    ])
    def test_stdin_mode(filename, mode, iter_by, allow_stdin, expanduser, expandvars):
        if filename == '-':
            with pytest.raises(TypeError):
                for line in islurp('-', mode=mode, iter_by=iter_by, allow_stdin=allow_stdin, expanduser=expanduser, expandvars=expandvars):
                    print(line)
        else:
            # Mock sys.stdin to simulate stdin input if needed
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_islurp_1_test_stdin_mode.py:23: Failed
----------------------------- Captured stdout call -----------------------------
Hello, world!
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_islurp_1_test_stdin_mode.py::test_stdin_mode[--r-100-True-True-True]
FAILED pytutils/Test4DT_tests/test_pytutils_files_islurp_1_test_stdin_mode.py::test_stdin_mode[example.txt-r-100-False-True-True]
FAILED pytutils/Test4DT_tests/test_pytutils_files_islurp_1_test_stdin_mode.py::test_stdin_mode[~/example.txt-r-100-False-True-True]
FAILED pytutils/Test4DT_tests/test_pytutils_files_islurp_1_test_stdin_mode.py::test_stdin_mode[$HOME/example.txt-r-100-False-True-True]
============================== 4 failed in 0.07s ===============================
"""
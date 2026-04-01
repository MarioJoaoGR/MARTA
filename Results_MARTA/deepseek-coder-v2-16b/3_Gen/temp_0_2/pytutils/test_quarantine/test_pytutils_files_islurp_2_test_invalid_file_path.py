
import pytest
from pytutils.files import islurp
from unittest.mock import patch
import sys

def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        # Test an invalid file path
        for _ in islurp('nonexistent_file.txt'):
            pass
    
    # Ensure that attempting to read from stdin is handled correctly
    with patch('sys.stdin', open('/dev/null')):  # Mocking sys.stdin as a file-like object
        with pytest.raises(EOFError):  # Since we're reading from an invalid stream, it should raise EOFError eventually
            for _ in islurp('-'):
                pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_files_islurp_2_test_invalid_file_path.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_file_path ____________________________

    def test_invalid_file_path():
        with pytest.raises(FileNotFoundError):
            # Test an invalid file path
            for _ in islurp('nonexistent_file.txt'):
                pass
    
        # Ensure that attempting to read from stdin is handled correctly
        with patch('sys.stdin', open('/dev/null')):  # Mocking sys.stdin as a file-like object
            with pytest.raises(EOFError):  # Since we're reading from an invalid stream, it should raise EOFError eventually
>               for _ in islurp('-'):

pytutils/Test4DT_tests/test_pytutils_files_islurp_2_test_invalid_file_path.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = '-', mode = 'r', iter_by = 0, allow_stdin = True, expanduser = True
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
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_islurp_2_test_invalid_file_path.py::test_invalid_file_path
============================== 1 failed in 0.07s ===============================
"""

import pytest
import sys
from pytutils.files import islurp

# Mocking sys.stdin for testing purposes
class StringIO:
    def __init__(self, string=""):
        self.string = string
        self.index = 0

    def readline(self):
        if self.index < len(self.string):
            line = self.string[self.index]
            self.index += 1
            return line
        else:
            return ''

    def read(self, size=None):
        if size is None or self.index + size > len(self.string):
            data = self.string[self.index:]
            self.index = len(self.string)
            return data
        else:
            data = self.string[self.index:self.index + size]
            self.index += size
            return data

@pytest.fixture
def mock_stdin():
    original_stdin = sys.stdin
    yield StringIO("line1\nline2\n")  # Mocked input for stdin
    sys.stdin = original_stdin

def test_valid_case_chunk_mode(mock_stdin):
    sys.stdin = mock_stdin  # Replace sys.stdin with the mocked StringIO object
    lines = list(islurp('-', iter_by=10))
    assert lines == ['line1\n', 'line2\n']

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

pytutils/Test4DT_tests/test_pytutils_files_islurp_0_test_valid_case_chunk_mode.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_chunk_mode __________________________

mock_stdin = <Test4DT_tests.test_pytutils_files_islurp_0_test_valid_case_chunk_mode.StringIO object at 0x7f3c11e3e310>

    def test_valid_case_chunk_mode(mock_stdin):
        sys.stdin = mock_stdin  # Replace sys.stdin with the mocked StringIO object
>       lines = list(islurp('-', iter_by=10))

pytutils/Test4DT_tests/test_pytutils_files_islurp_0_test_valid_case_chunk_mode.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = '-', mode = 'r', iter_by = 10, allow_stdin = True, expanduser = True
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
FAILED pytutils/Test4DT_tests/test_pytutils_files_islurp_0_test_valid_case_chunk_mode.py::test_valid_case_chunk_mode
============================== 1 failed in 0.06s ===============================
"""
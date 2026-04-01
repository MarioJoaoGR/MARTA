
import sys
import os
import functools
from pytutils.files import islurp

def test_valid_input_local_file():
    # Test reading a local file line by line
    with open('test_file.txt', 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")
    
    lines = []
    for line in islurp('test_file.txt'):
        lines.append(line)
    
    assert lines == ['Line 1\n', 'Line 2\n', 'Line 3']
    
    # Test reading from standard input (stdin)
    import io
    stdin = sys.stdin
    try:
        sys.stdin = io.StringIO("Input from stdin")
        lines_from_stdin = list(islurp('-'))
        assert lines_from_stdin == ['Input from stdin']
    finally:
        sys.stdin = stdin
    
    # Clean up the test file
    os.remove('test_file.txt')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
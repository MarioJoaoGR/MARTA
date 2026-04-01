
import pytest
from pytutils.iters import dedupe_iter

def test_valid_input():
    # Test with a list of integers
    input_list = [1, 2, 3, 2, 1]
    expected_output = [1, 2, 3]
    
    result = list(dedupe_iter(input_list))
    
    assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
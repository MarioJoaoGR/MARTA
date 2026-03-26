
import pytest
from pytutils.iters import accumulate
import operator

def test_valid_case_addition():
    assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
    assert list(accumulate([1, 2, 3, 4, 5], operator.mul)) == [1, 2, 6, 24, 120]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""

import pytest
from pytutils.iters import accumulate
import operator

def test_accumulate_empty_list():
    assert list(accumulate([])) == []

def test_accumulate_single_element():
    assert list(accumulate([1])) == [1]

def test_accumulate_default_func():
    assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]

def test_accumulate_custom_func():
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
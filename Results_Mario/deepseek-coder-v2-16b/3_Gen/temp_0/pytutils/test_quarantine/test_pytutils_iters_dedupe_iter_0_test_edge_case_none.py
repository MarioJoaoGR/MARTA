
import pytest
from pytutils.iters import dedupe_iter

def test_dedupe_iter():
    # Test with a list of integers
    result = list(dedupe_iter([1, 2, 3, 2, 1]))
    assert result == [1, 2, 3]

    # Test with a custom hash function
    def custom_hash(x):
        return x % 10
    
    result = list(dedupe_iter([11, 21, 31, 21, 11], custom_hash))
    assert result == [11, 21, 31]

    # Test with a string sequence
    result = list(dedupe_iter(['a', 'b', 'c', 'b', 'a']))
    assert result == ['a', 'b', 'c']

    # Test with an empty list
    result = list(dedupe_iter([]))
    assert result == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
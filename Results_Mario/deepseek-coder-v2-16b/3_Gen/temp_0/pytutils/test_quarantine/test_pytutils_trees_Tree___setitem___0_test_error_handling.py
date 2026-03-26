
import pytest
from pytutils.trees import Tree

def test_error_handling():
    tree = Tree({'a': {'b': 1}})
    
    # Test that an error is raised when trying to access a non-existent key
    with pytest.raises(KeyError):
        assert tree['c']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
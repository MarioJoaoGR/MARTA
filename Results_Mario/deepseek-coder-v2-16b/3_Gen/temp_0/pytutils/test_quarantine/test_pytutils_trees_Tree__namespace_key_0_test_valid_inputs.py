
import pytest
from pytutils.trees import Tree

def test_valid_inputs():
    t = Tree({'a': 1, 'b': {'c': 2}}, namespace='prefix')
    
    # Test accessing top-level keys
    assert t['a'] == 1
    assert t['b']['c'] == 2
    
    # Test accessing nested keys with the namespace prefix
    assert t['prefix:a'] == 1
    assert t['prefix:b']['prefix:c'] == 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
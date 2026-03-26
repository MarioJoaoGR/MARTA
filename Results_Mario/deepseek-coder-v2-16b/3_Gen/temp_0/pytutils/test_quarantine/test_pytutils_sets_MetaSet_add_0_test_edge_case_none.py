
import pytest
from pytutils.sets import MetaSet

def test_edge_case_none():
    meta_set = MetaSet()
    assert len(meta_set._store) == 0
    assert len(meta_set._meta) == 0
    
    # Add a value to trigger the _meta_func and see if it gets added to _meta
    meta_set.add(1)
    assert len(meta_set._store) == 1
    assert isinstance(list(meta_set._meta.values())[0], int)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
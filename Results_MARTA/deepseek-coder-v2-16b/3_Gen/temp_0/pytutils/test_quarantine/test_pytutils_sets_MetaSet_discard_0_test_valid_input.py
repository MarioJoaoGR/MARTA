
import pytest
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Add a value to the set
    meta_set.add(1)
    
    # Check that the value is in the set before discarding it
    assert 1 in meta_set._store
    
    # Discard the value
    meta_set.discard(1)
    
    # Check that the value has been removed from the set
    assert 1 not in meta_set._store

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
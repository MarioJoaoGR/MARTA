
import pytest
from pytutils.sets import MetaSet

def test_invalid_inputs():
    meta_set = MetaSet()
    
    # Adding invalid types should raise a TypeError
    with pytest.raises(TypeError):
        meta_set.add("string")  # string is not hashable, so it should raise a TypeError
        
    # Ensure the set remains empty after attempting to add an invalid type
    assert len(meta_set._store) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
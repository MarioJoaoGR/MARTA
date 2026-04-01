
import pytest
from pytutils.sets import MetaSet

def test_discard_invalid_input():
    meta_set = MetaSet()
    
    # Attempt to discard a value that is not in the set
    with pytest.raises(KeyError):
        meta_set.discard(1)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
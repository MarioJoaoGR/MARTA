
import pytest
from pytutils.sets import MetaSet
from datetime import datetime
import random
import attr

@pytest.fixture
def meta_set():
    return MetaSet()

def test_update(meta_set):
    lst = [1, 2, 3, 4]
    meta_set.update(lst)
    assert set(meta_set._store) == {1, 2, 3, 4}
    for item in lst:
        assert item in meta_set._store
        assert meta_set._meta[item]['added_at'] is not None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
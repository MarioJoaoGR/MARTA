
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_add(meta_set):
    value = "example_value"
    meta_set.add(value)
    assert len(meta_set._store) == 1
    assert value in meta_set._store
    assert isinstance(meta_set._meta[value], int)

def test_len(meta_set):
    assert len(meta_set) == 0
    meta_set.add("example_value")
    assert len(meta_set) == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
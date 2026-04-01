
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_none_input(meta_set):
    with pytest.raises(TypeError):
        meta_set.discard(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""

import pytest
from pytutils.sets import MetaSet
import random
import attr

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_inputs(meta_set):
    # Add some values to the MetaSet
    meta_set.add(1)
    meta_set.add(2)
    
    # Iterate over the MetaSet and check if it returns all added values with their respective timestamps
    for value in meta_set:
        assert value in meta_set._store
        assert value == meta_set._meta[value]['value']
        assert isinstance(meta_set._meta[value]['timestamp'], int)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
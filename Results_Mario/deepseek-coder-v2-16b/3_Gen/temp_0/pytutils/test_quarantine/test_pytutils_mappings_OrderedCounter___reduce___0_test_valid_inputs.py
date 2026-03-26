
import pytest
from pytutils.mappings import OrderedCounter
import pickle

def test_valid_inputs():
    oc = OrderedCounter()
    oc['a'] = 1
    oc['b'] = 2
    
    # Pickle the object
    pickled_oc = pickle.dumps(oc)
    
    # Unpickle the object
    unpickled_oc = pickle.loads(pickled_oc)
    
    # Assert that the unpickled object is equal to the original
    assert isinstance(unpickled_oc, OrderedCounter)
    assert list(unpickled_oc.items()) == [('a', 1), ('b', 2)]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
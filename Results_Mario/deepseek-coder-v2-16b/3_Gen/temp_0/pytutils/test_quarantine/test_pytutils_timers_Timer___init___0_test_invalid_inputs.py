
import pytest
from pytutils.timers import Timer

def test_invalid_inputs():
    # Test when name is not a string
    with pytest.raises(TypeError):
        with Timer(name=123, verbose=False):
            pass
    
    # Test when verbose is not a boolean
    with pytest.raises(TypeError):
        with Timer(name='test', verbose='True'):
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""

import pytest
from pytutils.timers import Timer

def test_valid_inputs():
    # Test initializing Timer with default values
    timer = Timer()
    assert timer.name == ''
    assert not timer.verbose

    # Test initializing Timer with custom name and verbose set to True
    timer = Timer(name='test_timer', verbose=True)
    assert timer.name == 'test_timer'
    assert timer.verbose

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
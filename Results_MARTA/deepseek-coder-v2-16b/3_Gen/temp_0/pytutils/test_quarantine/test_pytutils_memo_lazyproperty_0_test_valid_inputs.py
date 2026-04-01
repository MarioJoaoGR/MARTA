
import pytest
from pytutils.memo import lazyproperty

class MyClass:
    @lazyproperty
    def expensive_calculation(self):
        return sum(i**2 for i in range(1000))

def test_valid_inputs():
    obj = MyClass()
    
    # First call should compute the value
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))
    
    # Subsequent calls should use the cached result
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
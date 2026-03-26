
import pytest
from unittest.mock import patch, MagicMock
from pytutils.memo import lazyproperty

# Define a class with the lazy property
class MyClass:
    @lazyproperty
    def expensive_calculation(self):
        # This computation is expensive and only needed in certain circumstances
        return sum(i**2 for i in range(1000))

def test_lazyproperty():
    obj = MyClass()
    
    with patch.object(MyClass, 'expensive_calculation', MagicMock(return_value=499500)):
        # First call should compute the value
        assert obj.expensive_calculation == 499500
        
        # Subsequent calls should use the cached result
        assert obj.expensive_calculation == 499500

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
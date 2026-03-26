
import pytest
from pytutils.enum import LookupEnumMixin

def test_lookup_by_any_with_none():
    # Create a mock for the enum class that does not inherit from LookupEnumMixin
    class MockEnum(metaclass=type):
        pass
    
    with pytest.raises(TypeError) as excinfo:
        LookupEnumMixin.lookup_by_any(MockEnum)
    
    assert str(excinfo.value) == "Cannot call lookup_by_any() on a non-enum type"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
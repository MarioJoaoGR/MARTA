
import pytest
from pytutils.meth import bind

class Foo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def test_invalid_input():
    foo = Foo(2, 3)
    
    # Test with a non-callable object (should raise TypeError)
    with pytest.raises(TypeError):
        bind(foo, "not_a_function", 'multiply')
    
    # Test with an instance that is not an object (should raise TypeError)
    with pytest.raises(TypeError):
        bind("not_an_instance", lambda self: None, 'multiply')
    
    # Test with a non-string as_name (should raise TypeError)
    with pytest.raises(TypeError):
        bind(foo, lambda self: None, 123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""
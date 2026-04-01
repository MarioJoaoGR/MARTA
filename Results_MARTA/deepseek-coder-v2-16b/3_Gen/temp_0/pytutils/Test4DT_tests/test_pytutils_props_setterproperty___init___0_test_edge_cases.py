
import pytest
from pytutils.props import setterproperty

def test_setterproperty_init():
    def getter(self):
        return self._value
    
    sp = setterproperty(getter)
    assert hasattr(sp, 'func') and callable(getattr(sp, 'func'))
    assert sp.__doc__ == getter.__doc__

def test_setterproperty_init_with_doc():
    def getter(self):
        return self._value
    
    doc = "A custom documentation string."
    sp = setterproperty(getter, doc)
    assert hasattr(sp, 'func') and callable(getattr(sp, 'func'))
    assert sp.__doc__ == doc

def test_setterproperty_init_no_doc():
    def getter(self):
        return self._value
    
    sp = setterproperty(getter)
    assert hasattr(sp, 'func') and callable(getattr(sp, 'func'))
    assert sp.__doc__ == getter.__doc__

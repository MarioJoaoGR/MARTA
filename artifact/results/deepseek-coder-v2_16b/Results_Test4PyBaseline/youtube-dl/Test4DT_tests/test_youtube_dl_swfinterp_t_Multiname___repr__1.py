
import pytest
from youtube_dl.swfinterp import _Multiname

# Test case for initializing a multiname with the kind 'variable'
def test_multiname_init_with_variable():
    mn = _Multiname('variable')
    assert mn.kind == 'variable'

# Test case for accessing the __repr__ method of a multiname instance
def test_multiname_repr():
    mn = _Multiname('variable')
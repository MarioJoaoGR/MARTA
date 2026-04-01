
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_valid_inputs():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test attribute access
    assert b.whoa == True
    assert b.hello == [1, 2, 3]
    assert b.why == 'always'
    
    # Test setting new attributes
    b.state = 'new'
    assert hasattr(b, 'state')
    assert b.state == 'new'
    
    # Test nested attribute access
    b.subdict = dict(test=True)
    assert b.subdict.test == True
    
    # Test setting new attributes in nested structure
    b.subdict.nested_state = 'deep'
    assert b.subdict.nested_state == 'deep'
    
    # Ensure the original dictionary is not modified directly
    with pytest.raises(AttributeError):
        a.whoa = 'yeee'
    assert a['whoa'] == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_valid_inputs.py:21:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""

import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_valid_inputs():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test setting and getting values via key-based access
    assert 'whoa' in b
    assert b['whoa'] == True
    b['nice'] = False
    assert b['nice'] == False
    
    # Test attribute-style access
    assert hasattr(b, 'whoa')
    assert b.whoa == True
    b.state = 'new'
    assert b.state == 'new'
    
    # Test nested attributes
    b.subdict = dict(test=True)
    assert b.subdict.test == True
    
    # Ensure the changes are reflected in the original dictionary
    assert a['nice'] == False
    assert a['state'] == 'new'
    assert a['subdict']['test'] == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_valid_inputs.py:23:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""
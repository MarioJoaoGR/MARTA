
import pytest
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    def get_only(cls):
        return sentinel.get_only

@pytest.fixture
def z():
    return Z()

def test_edge_case(z):
    assert z.get_only() == sentinel.get_only

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_only_2_test_edge_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_2_test_edge_case.py:8:4: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)


"""
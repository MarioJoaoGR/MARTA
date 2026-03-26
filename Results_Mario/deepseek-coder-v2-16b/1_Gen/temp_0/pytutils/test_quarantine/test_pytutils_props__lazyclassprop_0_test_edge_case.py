
import pytest
from pytutils.props import _lazyclassprop

def test_edge_case():
    class MyClass:
        @_lazyclassprop
        def my_property(cls):
            print("Computing my_property")
            return 42

    obj = MyClass()
    
    # First call should compute the property
    assert obj.my_property == 42
    
    # Second call should retrieve the cached value
    assert obj.my_property == 42

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props__lazyclassprop_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_props__lazyclassprop_0_test_edge_case.py:3:0: E0611: No name '_lazyclassprop' in module 'pytutils.props' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_props__lazyclassprop_0_test_edge_case.py:8:8: E0213: Method 'my_property' should have "self" as first argument (no-self-argument)


"""
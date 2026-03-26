
import pytest
from pytutils.props import lazyclassproperty

def test_lazyclassproperty():
    class MyClass:
        @lazyclassproperty
        def expensive_calculation(cls):
            # This would be an expensive computation
            return sum(range(1000))
    
    obj = MyClass()
    
    # First call should compute and store the result
    assert obj.expensive_calculation == 499500
    
    # Subsequent calls should retrieve the cached result
    assert obj.expensive_calculation == 499500

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyclassproperty_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_edge_case.py:8:8: E0213: Method 'expensive_calculation' should have "self" as first argument (no-self-argument)


"""
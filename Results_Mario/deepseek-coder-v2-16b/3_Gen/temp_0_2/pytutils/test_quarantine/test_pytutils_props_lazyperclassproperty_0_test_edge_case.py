
import pytest
from pytutils.props import lazyperclassproperty, roclassproperty

def expensive_calculation(cls):
    return cls()

class MyClass1:
    pass

class MyClass2(MyClass1):
    pass

@lazyperclassproperty(expensive_calculation)
def cached_instance(cls):
    pass

# Test cases
def test_lazyperclassproperty():
    # First access will trigger the expensive calculation
    assert isinstance(MyClass1.cached_instance, MyClass1)
    assert not hasattr(MyClass2, 'cached_instance')  # Ensure it's only created for MyClass1
    
    # Subsequent accesses for the same class should return the cached result
    assert MyClass1.cached_instance is MyClass1.cached_instance
    
    # Different classes have separate instances
    assert isinstance(MyClass2.cached_instance, MyClass2)

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyperclassproperty_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_edge_case.py:21:22: E1101: Class 'MyClass1' has no 'cached_instance' member (no-member)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_edge_case.py:25:11: E1101: Class 'MyClass1' has no 'cached_instance' member (no-member)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_edge_case.py:25:39: E1101: Class 'MyClass1' has no 'cached_instance' member (no-member)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_edge_case.py:28:22: E1101: Class 'MyClass2' has no 'cached_instance' member (no-member)


"""
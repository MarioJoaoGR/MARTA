
import pytest
from pytutils.props import lazyclassproperty

def test_lazyclassproperty():
    class MyClass:
        @lazyclassproperty
        def expensive_calculation(cls):
            print("Calculating...")
            return sum(range(1000))
    
    # First access should trigger the calculation
    result = MyClass.expensive_calculation
    assert result == 499500, f"Expected 499500 but got {result}"
    
    # Subsequent accesses should return the cached value
    result2 = MyClass.expensive_calculation
    assert result2 == 499500, f"Expected 499500 but got {result2}"
    print("Test passed!")

# Run the test
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyclassproperty_0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_edge_cases.py:8:8: E0213: Method 'expensive_calculation' should have "self" as first argument (no-self-argument)


"""
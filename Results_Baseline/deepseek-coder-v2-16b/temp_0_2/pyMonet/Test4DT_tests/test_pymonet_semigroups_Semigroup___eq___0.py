# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Semigroup  # Assuming the module name is correct and the function is imported correctly

# Test cases for Semigroup class
def test_semigroup_init():
    s = Semigroup(5)
    assert s.value == 5

    s = Semigroup("hello")
    assert s.value == "hello"

# Additional test cases to ensure the equality method works correctly
def test_semigroup_equality():
    s1 = Semigroup(5)
    s2 = Semigroup(5)
    assert s1 == s2

    s3 = Semigroup(10)
    assert not (s1 == s3)

# Edge cases to check the behavior with different types and values
def test_semigroup_edge_cases():
    # Test with a complex type
    s = Semigroup([1, 2, 3])
    assert s.value == [1, 2, 3]

    # Test with None
    s = Semigroup(None)
    assert s.value is None

# Run the tests when this script is executed
if __name__ == "__main__":
    pytest.main()

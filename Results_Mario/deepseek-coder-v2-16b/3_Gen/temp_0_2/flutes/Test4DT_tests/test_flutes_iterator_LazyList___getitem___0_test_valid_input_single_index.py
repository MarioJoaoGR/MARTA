
import pytest
from flutes.iterator import LazyList

# Assuming that 'flutes.iterator' contains the implementation of LazyList and its iterator logic

def test_valid_input_single_index():
    # Create an instance of LazyList with a sample iterable
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Test accessing a single index
    assert lazy_list[0] == 1
    assert lazy_list[1] == 2
    assert lazy_list[2] == 3
    assert lazy_list[3] == 4

# Run the test if this script is executed directly
if __name__ == "__main__":
    pytest.main()

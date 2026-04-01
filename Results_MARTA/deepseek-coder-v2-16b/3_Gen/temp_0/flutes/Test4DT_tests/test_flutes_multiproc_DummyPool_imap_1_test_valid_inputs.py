
import pytest
from flutes.multiproc import DummyPool  # Assuming this is the correct module and path

def test_valid_inputs():
    """Test that DummyPool accepts valid inputs correctly."""
    
    # Test initialization with default values
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool), "Expected a DummyPool instance"
    
    # Test imap method with a simple function and iterable
    def multiply_by_two(x):
        return x * 2
    
    results = pool.imap(multiply_by_two, range(5))
    expected_results = [0, 2, 4, 6, 8]
    assert list(results) == expected_results, "Expected imap to apply the function correctly"

# Run the test if this script is executed directly
if __name__ == "__main__":
    pytest.main([__file__])

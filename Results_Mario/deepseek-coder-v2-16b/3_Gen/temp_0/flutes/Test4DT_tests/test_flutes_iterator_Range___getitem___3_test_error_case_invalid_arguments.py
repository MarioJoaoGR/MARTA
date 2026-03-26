
import pytest
from flutes.iterator import Range

def test_error_case_invalid_arguments():
    with pytest.raises(ValueError):
        r = Range()  # No arguments provided
        r[0]         # Accessing an item without raising ValueError should fail the test

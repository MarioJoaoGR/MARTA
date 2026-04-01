
import pytest
from flutes.iterator import Range

def test_error_case_invalid_arguments():
    with pytest.raises(ValueError):
        Range()  # No arguments provided
        Range(1, 2, 3, 4)  # More than three arguments provided

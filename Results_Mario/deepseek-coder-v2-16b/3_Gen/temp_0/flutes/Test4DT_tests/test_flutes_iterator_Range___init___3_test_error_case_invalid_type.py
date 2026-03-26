
import pytest
from flutes.iterator import Range

def test_error_case_invalid_type():
    with pytest.raises(ValueError):
        Range()  # No arguments provided, should raise ValueError

    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)  # More than three arguments provided, should raise ValueError

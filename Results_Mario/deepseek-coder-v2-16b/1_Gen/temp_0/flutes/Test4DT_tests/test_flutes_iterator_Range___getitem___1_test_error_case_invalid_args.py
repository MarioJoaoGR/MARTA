
import pytest
from flutes.iterator import Range

def test_error_case_invalid_args():
    with pytest.raises(ValueError):
        r = Range()  # No arguments provided
        r[0]         # This should raise a ValueError

    with pytest.raises(ValueError):
        r = Range(1, 2, 3, 4)  # More than three arguments provided
        r[0]                   # This should raise a ValueError

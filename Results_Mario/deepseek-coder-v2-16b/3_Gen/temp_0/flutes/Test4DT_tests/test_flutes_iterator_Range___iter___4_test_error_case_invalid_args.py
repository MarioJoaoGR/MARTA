
import pytest
from flutes import Range

def test_error_case_invalid_args():
    with pytest.raises(ValueError):
        r = Range()  # No arguments provided
        list(r)       # This should raise a ValueError

    with pytest.raises(ValueError):
        r = Range(1, 2, 3, 4)  # More than three arguments provided
        list(r)                 # This should raise a ValueError

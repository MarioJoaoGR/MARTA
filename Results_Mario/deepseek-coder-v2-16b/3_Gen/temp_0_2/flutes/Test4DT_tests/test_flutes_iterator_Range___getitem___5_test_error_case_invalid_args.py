
import pytest
from flutes.iterator import Range

def test_error_case_invalid_args():
    with pytest.raises(ValueError):
        r = Range()  # No arguments provided, should raise ValueError
        r[0]         # Accessing an item should also raise ValueError due to invalid initialization


import pytest
from flutes.iterator import Range

def test_error_case_invalid_type():
    with pytest.raises(ValueError):
        r = Range()  # No arguments provided, should raise ValueError


import pytest
from flutes import Range

def test_error_case_invalid_args():
    with pytest.raises(ValueError):
        r = Range()  # No arguments provided
        assert False, "Expected a ValueError when no arguments are given"

    with pytest.raises(ValueError):
        r = Range(1, 2, 3, 4)  # More than three arguments provided
        assert False, "Expected a ValueError when more than three arguments are given"

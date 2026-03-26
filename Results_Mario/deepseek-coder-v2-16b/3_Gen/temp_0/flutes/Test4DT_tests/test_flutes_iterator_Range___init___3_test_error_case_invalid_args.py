
import pytest
from flutes.iterator import Range  # Assuming this is the correct module path

def test_error_case_invalid_args():
    with pytest.raises(ValueError):
        r = Range()          # No arguments provided
        assert False, "Expected ValueError for no arguments"
    with pytest.raises(ValueError):
        r = Range(1, 2, 3, 4) # More than three arguments provided
        assert False, "Expected ValueError for more than three arguments"
    try:
        r = Range(10)         # One argument provided (end)
        assert isinstance(r, Range), "Expected an instance of Range"
        assert r.l == 0, f"Expected start to be 0 but got {r.l}"
        assert r.r == 10, f"Expected end to be 10 but got {r.r}"
        assert r.step == 1, f"Expected step to be 1 but got {r.step}"
    except ValueError:
        pytest.fail("Unexpected ValueError for one argument")
    try:
        r = Range(1, 10)      # Two arguments provided (start and end)
        assert isinstance(r, Range), "Expected an instance of Range"
        assert r.l == 1, f"Expected start to be 1 but got {r.l}"
        assert r.r == 10, f"Expected end to be 10 but got {r.r}"
        assert r.step == 1, f"Expected step to be 1 but got {r.step}"
    except ValueError:
        pytest.fail("Unexpected ValueError for two arguments")
    try:
        r = Range(1, 10, 2)   # Three arguments provided (start, end, and step)
        assert isinstance(r, Range), "Expected an instance of Range"
        assert r.l == 1, f"Expected start to be 1 but got {r.l}"
        assert r.r == 10, f"Expected end to be 10 but got {r.r}"
        assert r.step == 2, f"Expected step to be 2 but got {r.step}"
    except ValueError:
        pytest.fail("Unexpected ValueError for three arguments")

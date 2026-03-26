
import pytest
from flutes.iterator import Range

def test_valid_case_one_argument():
    r = Range(10)
    assert isinstance(r, Range), "Instance should be of type Range"
    assert r.l == 0, "Start should default to 0 when only one argument is provided"
    assert r.r == 10, "End should be the value of the single argument"
    assert r.step == 1, "Step should default to 1 when only one argument is provided"
    assert len(r) == 10, "Length should be calculated as end - start"

if __name__ == "__main__":
    pytest.main()


import pytest
from pytutils.sets import TimedValueSet  # Correctly import from the specified module path

def test_invalid_input():
    tvs = TimedValueSet()
    with pytest.raises(TypeError):  # Expect a TypeError when calling added_at without arguments
        tvs.added_at()

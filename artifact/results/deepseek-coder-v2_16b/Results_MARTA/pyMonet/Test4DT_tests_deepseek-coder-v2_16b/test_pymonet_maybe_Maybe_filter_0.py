
import pytest
from pymonet.maybe import Maybe

# Test valid input scenario
def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    filtered = maybe_some.filter(lambda x: isinstance(x, int))
    assert not filtered.is_nothing
    assert filtered.value == 42

# Test edge case with None value in Maybe scenario
def test_edge_case_none():
    maybe_none = Maybe(value=None, is_nothing=True)
    filtered = maybe_none.filter(lambda x: isinstance(x, int))
    assert filtered.is_nothing

# Test invalid input by providing a non-callable filterer scenario
def test_invalid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    with pytest.raises(TypeError):
        maybe_some.filter("not a callable")

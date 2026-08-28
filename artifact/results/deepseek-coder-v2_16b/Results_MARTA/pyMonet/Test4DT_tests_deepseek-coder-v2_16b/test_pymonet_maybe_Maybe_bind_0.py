
import pytest
from pymonet.maybe import Maybe

# Scenario 1: Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

# Scenario 2: Test edge case where input is None resulting in an empty Maybe
def test_edge_case_none():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing
    with pytest.raises(AttributeError):
        maybe_none.value  # This should raise an AttributeError because the value shouldn't be accessible when is_nothing is True

# Scenario 3: Test invalid input where the mapper function raises an exception
def test_invalid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    def raising_mapper(x):
        raise ValueError("Mapper function error")
    
    with pytest.raises(ValueError):
        maybe_some.bind(raising_mapper)  # This should raise a ValueError because the mapper function raises an exception

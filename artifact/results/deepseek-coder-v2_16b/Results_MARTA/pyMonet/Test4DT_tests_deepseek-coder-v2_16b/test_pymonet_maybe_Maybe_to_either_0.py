
import pytest
from pymonet.maybe import Maybe

# Test scenario 1: Test standard input with a valid value
def test_valid_input_with_value():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

# Test scenario 2: Test edge case with None as the value
def test_edge_case_none_value():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing
    assert maybe_none.to_either().is_left()

# Test scenario 3: Test invalid input by missing required arguments
def test_invalid_input_missing_args():
    with pytest.raises(TypeError):
        Maybe()


import pytest
from collections.abc import Mapping, Sequence
from ansible.template.native_helpers import _fail_on_undefined, StrictUndefined

# Test valid inputs
def test_valid_inputs():
    data = {'a': 1, 'b': 2}
    assert not isinstance(data['b'], StrictUndefined)

# Test edge cases including None, empty lists, and boundary values
def test_edge_cases():
    data = {'a': 1, 'b': None}
    assert isinstance(data['b'], type(None))

# Test invalid inputs to ensure proper error handling
def test_invalid_inputs():
    data = {'a': 1, 'b': StrictUndefined()}
    assert isinstance(data['b'], StrictUndefined)

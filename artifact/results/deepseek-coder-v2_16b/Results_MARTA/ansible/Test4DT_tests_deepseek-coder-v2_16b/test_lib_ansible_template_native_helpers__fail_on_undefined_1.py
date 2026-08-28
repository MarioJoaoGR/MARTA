
import pytest
from ansible.template.native_helpers import StrictUndefined

# Scenario 1: Test standard input with a dictionary containing no undefined values
def test_valid_input():
    data = {'a': 1, 'b': 2}
    assert _fail_on_undefined(data) == data

# Scenario 2: Test nested structure with one undefined value
def test_undefined_in_nested_structure():
    nested_data = {'dict1': {'key1': 1, 'key2': StrictUndefined()}, 'list1': [0, 1, 2, StrictUndefined()]}
    with pytest.raises(StrictUndefined):
        _fail_on_undefined(nested_data)

# Scenario 3: Test mixed structure with different types including undefined value
def test_undefined_in_mixed_structure():
    mixed_data = {'int': 42, 'dict': {'innerKey': StrictUndefined()}, 'list': [1, 2, None, StrictUndefined()]}
    with pytest.raises(StrictUndefined):
        _fail_on_undefined(mixed_data)

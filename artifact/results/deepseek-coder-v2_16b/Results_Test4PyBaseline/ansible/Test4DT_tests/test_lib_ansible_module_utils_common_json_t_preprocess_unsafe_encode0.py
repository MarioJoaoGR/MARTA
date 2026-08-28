
import pytest
from ansible.module_utils.common.json import _preprocess_unsafe_encode

# Helper function to simulate the behavior of _is_unsafe and to_text functions
def is_sequence(value):
    return isinstance(value, list) or isinstance(value, tuple)

def to_text(value, errors='surrogate_or_strict', nonstring='strict'):
    if isinstance(value, bytes):
        value = value.decode('utf-8')
    return value

# Test cases for _preprocess_unsafe_encode function
@pytest.mark.parametrize("input_value, expected", [
    # Simple call with AnsibleUnsafe instance
    ({"__ansible_unsafe": "sensitive data"}, {'__ansible_unsafe': 'sensitive data'}),
    
    # Nested structure with AnsibleUnsafe instances
    ([{"__ansible_unsafe": "data1"}, {"__ansible_unsafe": "data2"}], [{'__ansible_unsafe': 'data1'}, {'__ansible_unsafe': 'data2'}]),
    
    # Handling a non-unsafe value (should return the value as is)
    ("normal data", "normal data"),
    
    # Handling an empty structure
    ([], []),
    
    # Handling a dictionary with AnsibleUnsafe instances
    ({'key1': {"__ansible_unsafe": "value1"}, 'key2': {"__ansible_unsafe": "value2"}}, {'key1': {'__ansible_unsafe': 'value1'}, 'key2': {'__ansible_unsafe': 'value2'}}),
])
def test_preprocess_unsafe_encode(input_value, expected):
    assert _preprocess_unsafe_encode(input_value) == expected

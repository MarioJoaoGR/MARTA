
import pytest
from typesystem.schemas import Reference

# Scenario 1: Test standard input with valid schema definitions
def test_valid_inputs():
    ref = Reference("example_schema", definitions={'key': 'value'})
    assert len(ref.definitions) == 1
    assert ref.definitions['key'] == 'value'

# Scenario 2: Test invalid input type
def test_invalid_input():
    ref = Reference("example_schema", definitions={'key': 'value'})
    obj = 'not a dictionary'
    with pytest.raises(ValueError):
        ref.serialize(obj)

# Scenario 3: Test serialization of None object
def test_serialize_none():
    ref = Reference("example_schema", definitions={'key': 'value'})
    assert ref.serialize(None) is None

# Scenario 4: Test serialization with valid dictionary input
def test_serialize_valid_dict():
    ref = Reference("example_schema", definitions={'key': 'value'})
    obj = {'key': 'value'}
    serialized = ref.serialize(obj)
    assert isinstance(serialized, dict)
    assert serialized == {'key': 'value'}

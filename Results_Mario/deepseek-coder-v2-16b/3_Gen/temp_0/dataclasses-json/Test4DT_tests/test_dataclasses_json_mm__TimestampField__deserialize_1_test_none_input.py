
from dataclasses_json.mm import _TimestampField, ValidationError

def test_none_input():
    field = _TimestampField()
    assert field._deserialize(None, attr="test_attr", data={}) is None

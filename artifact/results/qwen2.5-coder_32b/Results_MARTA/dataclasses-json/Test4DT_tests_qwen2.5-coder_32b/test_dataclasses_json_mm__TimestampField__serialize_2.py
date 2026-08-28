
import pytest
from datetime import datetime
from dataclasses_json.mm import _TimestampField, ValidationError



def test_none_value_not_required():
    ts_field = _TimestampField(required=False)
    assert ts_field._serialize(None, 'created_at', None) is None

def test_none_value_required_raises_validation_error():
    ts_field_required = _TimestampField(required=True)
    with pytest.raises(ValidationError):
        ts_field_required._serialize(None, 'created_at', None)
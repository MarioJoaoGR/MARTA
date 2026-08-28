
import pytest
from datetime import datetime
from dataclasses_json.mm import _TimestampField, ValidationError



def test_non_required_field_with_none():
    ts_field = _TimestampField(required=False)
    assert ts_field._serialize(None, 'created_at', None) is None

def test_required_field_with_none_raises_validation_error():
    ts_field = _TimestampField(required=True)
    with pytest.raises(ValidationError):
        ts_field._serialize(None, 'created_at', None)
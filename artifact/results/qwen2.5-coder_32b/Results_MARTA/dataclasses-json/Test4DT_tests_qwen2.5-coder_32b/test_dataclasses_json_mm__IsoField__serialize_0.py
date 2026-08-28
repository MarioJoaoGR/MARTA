
import pytest
from datetime import datetime
from dataclasses_json.mm import _IsoField, ValidationError

def test_serialize_datetime_required():
    iso_field = _IsoField(required=True)
    value = datetime(2023, 10, 5, 14, 48)
    serialized_value = iso_field._serialize(value, 'date', None)
    assert serialized_value == '2023-10-05T14:48:00'

def test_serialize_datetime_not_required():
    iso_field = _IsoField(required=False)
    value = datetime(2023, 10, 5, 14, 48)
    serialized_value = iso_field._serialize(value, 'date', None)
    assert serialized_value == '2023-10-05T14:48:00'

def test_serialize_none_not_required():
    iso_field = _IsoField(required=False)
    value = None
    serialized_value = iso_field._serialize(value, 'date', None)
    assert serialized_value is None

def test_serialize_none_required():
    iso_field = _IsoField(required=True)
    value = None
    with pytest.raises(ValidationError) as excinfo:
        iso_field._serialize(value, 'date', None)
    assert str(excinfo.value) == "Missing data for required field."

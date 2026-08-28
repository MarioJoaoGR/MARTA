# Module: dataclasses_json.mm
import pytest
from datetime import datetime
from dataclasses_json.mm import _IsoField, ValidationError

def test_serialize_non_required_field_with_datetime():
    iso_field = _IsoField()
    iso_field.required = False
    iso_field.default_error_messages = {"required": "This field is required."}
    dt_obj = datetime(2023, 9, 15, 14, 30)
    assert iso_field._serialize(dt_obj, 'created_at', None) == '2023-09-15T14:30:00'

def test_serialize_required_field_with_datetime():
    iso_field = _IsoField()
    iso_field.required = True
    iso_field.default_error_messages = {"required": "This field is required."}
    dt_obj = datetime(2023, 9, 15, 14, 30)
    assert iso_field._serialize(dt_obj, 'created_at', None) == '2023-09-15T14:30:00'

def test_serialize_required_field_with_none():
    iso_field = _IsoField()
    iso_field.required = True
    iso_field.default_error_messages = {"required": "This field is required."}
    with pytest.raises(ValidationError, match="This field is required."):
        iso_field._serialize(None, 'created_at', None)

def test_serialize_non_required_field_with_none():
    iso_field = _IsoField()
    iso_field.required = False
    iso_field.default_error_messages = {"required": "This field is required."}
    assert iso_field._serialize(None, 'created_at', None) is None

def test_serialize_with_custom_error_message():
    iso_field = _IsoField()
    iso_field.required = True
    iso_field.default_error_messages = {"required": "Custom error message."}
    with pytest.raises(ValidationError, match="Custom error message."):
        iso_field._serialize(None, 'created_at', None)

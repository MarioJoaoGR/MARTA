
# Test case  
import pytest
from datetime import datetime
from dataclasses_json.mm import _IsoField, ValidationError

class Test_IsoFieldDeserialize:

    def setup_method(self):
        self.iso_field = _IsoField()
        self.iso_field.required = False
        self.iso_field.default_error_messages = {"required": "This field is required."}

    def test_deserialize_valid_iso_string(self):
        iso_string = "2023-10-05T14:48:00"
        result = self.iso_field._deserialize(iso_string, 'date_attr', {})
        assert result == datetime(2023, 10, 5, 14, 48)

    def test_deserialize_none_not_required(self):
        result = self.iso_field._deserialize(None, 'date_attr', {})
        assert result is None

    def test_deserialize_none_required(self):
        self.iso_field.required = True
        with pytest.raises(ValidationError) as excinfo:
            self.iso_field._deserialize(None, 'date_attr', {})
        assert str(excinfo.value) == "This field is required."

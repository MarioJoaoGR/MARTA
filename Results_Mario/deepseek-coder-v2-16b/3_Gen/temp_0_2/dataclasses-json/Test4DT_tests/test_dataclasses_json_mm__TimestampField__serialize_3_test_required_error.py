
# Import necessary modules and classes
from dataclasses_json.mm import ValidationError  # Correctly importing ValidationError from the specified module
import pytest
from datetime import datetime

# Define the _TimestampField class and its serialize method as provided in your scenario
class _TimestampField:
    def __init__(self, required=True):
        self.required = required
        self.default_error_messages = {"required": "This field is required"}
    
    def _serialize(self, value, attr, obj, **kwargs):
        if value is not None:
            return value.timestamp()
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

# Define the test case for required error scenario
def test_required_error():
    field = _TimestampField(required=True)  # Create an instance of _TimestampField with required set to True
    
    # Test when value is None and it's a required field
    with pytest.raises(ValidationError) as excinfo:
        field._serialize(value=None, attr="test_attr", obj={})
    assert str(excinfo.value) == "This field is required"  # Check if the error message matches the expected one

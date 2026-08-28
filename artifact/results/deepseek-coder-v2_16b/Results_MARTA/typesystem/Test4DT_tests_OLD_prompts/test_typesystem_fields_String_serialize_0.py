
import pytest
from typesystem.fields import String, ValidationError

# Test allowing blank values in a string field

# Test validating an invalid type (non-string) should raise ValidationError
def test_invalid_type():
    string_field = String(allow_blank=True)
    with pytest.raises(ValidationError) as excinfo:
        string_field.validate(12345)
    assert str(excinfo.value) == "Must be a string."
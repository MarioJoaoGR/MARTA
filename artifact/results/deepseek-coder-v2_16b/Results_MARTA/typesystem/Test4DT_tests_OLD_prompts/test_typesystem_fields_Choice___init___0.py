
import pytest
from typesystem.fields import Choice, ValidationError

# Test for validating a non-strict None input

# Test for validating a strict None input and expecting a ValidationError
def test_none_input():
    choice_instance = Choice(choices=[("Option1", "action1"), ("Option2", "action2")])
    with pytest.raises(ValidationError) as e:
        validated_none = choice_instance.validate(None, strict=True)
    assert str(e.value) == 'May not be null.', f"Expected ValidationError for None input but got {str(e.value)}"
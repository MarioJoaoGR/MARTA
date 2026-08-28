
import pytest
from typesystem.fields import Choice

# Scenario 1: Test standard input with valid schema definitions
def test_valid_choices():
    choice = Choice(choices=[("Option1", "action1"), ("Option2", "action2")])
    assert choice.validate("Option1") == "Option1"
    assert choice.validate("Option2") == "Option2"

# Scenario 2: Test handling of invalid choices in strict mode
def test_invalid_choice_strict():
    choice = Choice(choices=[("Option1", "action1"), ("Option2", "action2")])
    with pytest.raises(Exception) as excinfo:
        choice.validate("InvalidOption")
    assert str(excinfo.value) == 'Not a valid choice.'

# Scenario 3: Test allowing null values and handling None input
def test_allow_null():
    choice = Choice(choices=[("Option1", "action1"), ("Option2", "action2")])
    with pytest.raises(Exception) as excinfo:
        choice.validate(None, strict=True)
    assert str(excinfo.value) == 'May not be null.'

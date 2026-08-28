
import pytest
from typesystem.composites import Not
from typesystem.fields import Field

# Scenario 1: Test initialization with valid `Field` instance
def test_valid_init():
    field = Field()
    not_field = Not(negated=field)
    assert isinstance(not_field, Not)
    assert not_field.negated == field

# Scenario 2: Test initialization with invalid type raises AssertionError

import pytest
from typesystem.fields import Field, NO_DEFAULT
import typing

def test_get_default_value_no_default():
    field = Field()
    assert field.get_default_value() is None

def test_get_default_value_with_callable_default():
    def default_factory():
        return 42
    field = Field(default=default_factory)
    assert field.get_default_value() == 42

def test_get_default_value_with_non_callable_default():
    field = Field(default="some value")
    assert field.get_default_value() == "some value"

def test_get_default_value_with_none_default():
    field = Field(default=None)
    assert field.get_default_value() is None

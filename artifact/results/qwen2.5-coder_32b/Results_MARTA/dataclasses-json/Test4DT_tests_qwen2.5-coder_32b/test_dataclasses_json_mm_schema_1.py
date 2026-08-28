
import pytest
from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json.mm import schema

@dataclass
class MyMixin:
    pass

@dataclass
class User(MyMixin):
    name: str = 'default_name'
    age: int = 0
    email: Optional[str] = None

def test_happy_path():
    user_schema = schema(User, MyMixin, True)
    assert isinstance(user_schema['name'], type(user_schema['name']))
    assert isinstance(user_schema['age'], type(user_schema['age']))

def test_optional_field_included():
    user_schema = schema(User, MyMixin, True)
    assert 'email' in user_schema

def test_default_value_with_infer_missing():
    user_schema = schema(User, MyMixin, True)
    assert user_schema['name'].load_default == 'default_name'
    assert user_schema['age'].load_default == 0

def test_default_value_without_infer_missing():
    user_schema = schema(User, MyMixin, False)
    assert user_schema['name'].dump_default == 'default_name'
    assert user_schema['age'].dump_default == 0

def test_optional_field_with_none():
    user_schema = schema(User, MyMixin, True)
    assert user_schema['email'].allow_none is True

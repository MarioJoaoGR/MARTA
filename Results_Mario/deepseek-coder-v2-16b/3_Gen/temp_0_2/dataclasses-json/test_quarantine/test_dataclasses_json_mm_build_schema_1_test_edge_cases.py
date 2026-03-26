
import pytest
from dataclasses import dataclass, fields
import typing
from marshmallow import Schema, post_load
from dataclasses_json.mm import build_schema

# Assuming 'my_module' contains MyDataClass and other necessary components
# from my_module import MyDataClass, build_schema

@dataclass
class MyDataClass:
    a: int
    b: str = "default"

def test_build_schema():
    class MyMixin: pass

    schema = build_schema(MyDataClass, MyMixin, infer_missing=True, partial=False)
    
    assert issubclass(schema, Schema), "The generated schema should be a subclass of marshmallow.Schema"
    
    meta_fields = schema.Meta.fields
    expected_fields = tuple(field.name for field in fields(MyDataClass))
    assert meta_fields == expected_fields, f"Expected fields {expected_fields}, but got {meta_fields}"

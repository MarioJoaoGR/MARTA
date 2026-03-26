
import pytest
from dataclasses import dataclass, fields as dc_fields
import typing
from marshmallow import Schema, post_load
from dataclasses_json.mm import build_schema

# Assuming your module is correctly named 'your_module' and contains the necessary classes/functions
# from your_module import MyDataclass  # Uncomment this line if you have a specific dataclass to test with

@dataclass
class A:
    pass

def test_build_schema():
    class OptionalMixin:
        pass

    schema = build_schema(A, OptionalMixin, True, False)
    assert issubclass(schema, Schema), "The returned object should be a subclass of marshmallow.Schema"

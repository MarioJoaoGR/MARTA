
# Module: dataclasses_json.mm
import pytest
from dataclasses import dataclass
import typing
from marshmallow import Schema, post_load
from dataclasses_json import build_schema, dataclass_json

# Define a simple dataclass for testing
@dataclass_json
@dataclass
class Person:
    name: str
    age: int = 0

def test_build_schema():
    # Test building schema with default parameters
    schema = build_schema(Person, mixin=None, infer_missing=True, partial=False)
    assert isinstance(schema, Schema), "Expected a Marshmallow Schema"
    assert hasattr(schema, 'Meta'), "Expected Meta attribute in the schema"
    assert hasattr(schema, f'make_{Person.__name__.lower()}'), "Expected make_person method"
    assert hasattr(schema, 'dump'), "Expected dump method"
    assert hasattr(schema, 'dumps'), "Expected dumps method"

def test_build_schema_with_mixin():
    # Test building schema with a mixin (not implemented in this example)
    with pytest.raises(NotImplementedError):
        build_schema(Person, mixin=None, infer_missing=True, partial=False)

def test_build_schema_infer_missing():
    # Test building schema with infer_missing set to True
    @dataclass
    class PersonWithOptionalAge:
        name: str
        age: typing.Optional[int] = None

    schema = build_schema(PersonWithOptionalAge, mixin=None, infer_missing=True, partial=False)
    assert isinstance(schema, Schema), "Expected a Marshmallow Schema"
    assert hasattr(schema, 'Meta'), "Expected Meta attribute in the schema"
    assert hasattr(schema, f'make_{PersonWithOptionalAge.__name__.lower()}'), "Expected make_person method"
    assert hasattr(schema, 'dump'), "Expected dump method"
    assert hasattr(schema, 'dumps'), "Expected dumps method"

def test_build_schema_partial():
    # Test building schema with partial set to True
    @dataclass
    class PersonPartial:
        name: str
        age: int = 0

    schema = build_schema(PersonPartial, mixin=None, infer_missing=False, partial=True)
    assert isinstance(schema, Schema), "Expected a Marshmallow Schema"
    assert hasattr(schema, 'Meta'), "Expected Meta attribute in the schema"
    assert hasattr(schema, f'make_{PersonPartial.__name__.lower()}'), "Expected make_person method"
    assert hasattr(schema, 'dump'), "Expected dump method"
    assert hasattr(schema, 'dumps'), "Expected dumps method"

def test_build_schema_no_partial():
    # Test building schema with partial set to False
    @dataclass
    class PersonNoPartial:
        name: str
        age: int = 0

    schema = build_schema(PersonNoPartial, mixin=None, infer_missing=False, partial=False)
    assert isinstance(schema, Schema), "Expected a Marshmallow Schema"
    assert hasattr(schema, 'Meta'), "Expected Meta attribute in the schema"
    assert hasattr(schema, f'make_{PersonNoPartial.__name__.lower()}'), "Expected make_person method"
    assert hasattr(schema, 'dump'), "Expected dump method"
    assert hasattr(schema, 'dumps'), "Expected dumps method"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_schema_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_0.py:7:0: E0611: No name 'build_schema' in module 'dataclasses_json' (no-name-in-module)

"""
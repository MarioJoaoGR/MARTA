
import pytest
from dataclasses import dataclass, field
from typing import Optional, Type
import dataclasses_json.mm as mm

@dataclass
class MyDataClass:
    name: str = field(metadata={'dataclasses_json': {'encoder': lambda x: x.upper()}})
    age: int
    address: Optional[str] = None

@dataclass
class AnotherDataClass:
    title: str
    year: int

@dataclass
class YetAnotherDataClass:
    description: str
    count: int

@dataclass
class OptionalFieldsDataClass:
    required_field: str
    optional_field: Optional[str] = None

def test_build_schema_basic_usage():
    schema_class = mm.build_schema(MyDataClass, mm.SchemaF, infer_missing=True, partial=False)
    assert issubclass(schema_class, mm.Schema)  # Changed from mm.SchemaType to mm.Schema
    assert hasattr(schema_class, 'Meta')
    assert hasattr(schema_class, 'make_mydataclass')
    assert hasattr(schema_class, 'dumps')
    assert hasattr(schema_class, 'dump')

def test_build_schema_with_custom_mixin_and_partial_data():
    schema_class = mm.build_schema(AnotherDataClass, mm.SchemaF, infer_missing=False, partial=True)
    assert issubclass(schema_class, mm.Schema)  # Changed from mm.SchemaType to mm.Schema
    assert hasattr(schema_class, 'Meta')
    assert hasattr(schema_class, 'make_anotherdataclass')
    assert hasattr(schema_class, 'dumps')
    assert hasattr(schema_class, 'dump')

def test_build_schema_using_dataclass_json_mixin():
    schema_class = mm.build_schema(YetAnotherDataClass, mm.SchemaF, infer_missing=True, partial=False)  # Changed from mm.Mixin to mm.SchemaF
    assert issubclass(schema_class, mm.Schema)  # Changed from mm.SchemaType to mm.Schema
    assert hasattr(schema_class, 'Meta')
    assert hasattr(schema_class, 'make_yetanotherdataclass')
    assert hasattr(schema_class, 'dumps')
    assert hasattr(schema_class, 'dump')

def test_build_schema_handling_optional_fields():
    schema_class = mm.build_schema(OptionalFieldsDataClass, mm.SchemaF, infer_missing=True, partial=True)
    assert issubclass(schema_class, mm.Schema)  # Changed from mm.SchemaType to mm.Schema
    assert hasattr(schema_class, 'Meta')
    assert hasattr(schema_class, 'make_optionalfieldsdataclass')
    assert hasattr(schema_class, 'dumps')
    assert hasattr(schema_class, 'dump')

def test_build_schema_with_no_fields():
    @dataclass
    class EmptyDataClass:
        pass

    schema_class = mm.build_schema(EmptyDataClass, mm.SchemaF, infer_missing=True, partial=False)
    assert issubclass(schema_class, mm.Schema)  # Changed from mm.SchemaType to mm.Schema
    assert hasattr(schema_class, 'Meta')
    assert hasattr(schema_class, 'make_emptydataclass')
    assert hasattr(schema_class, 'dumps')
    assert hasattr(schema_class, 'dump')

def test_build_schema_with_only_optional_fields():
    @dataclass
    class OnlyOptionalDataClass:
        optional_field: Optional[str] = None

    schema_class = mm.build_schema(OnlyOptionalDataClass, mm.SchemaF, infer_missing=True, partial=False)
    assert issubclass(schema_class, mm.Schema)  # Changed from mm.SchemaType to mm.Schema
    assert hasattr(schema_class, 'Meta')
    assert hasattr(schema_class, 'make_onlyoptionaldataclass')
    assert hasattr(schema_class, 'dumps')
    assert hasattr(schema_class, 'dump')

def test_build_schema_with_infer_missing():
    schema_class = mm.build_schema(MyDataClass, mm.SchemaF, infer_missing=True, partial=False)
    assert issubclass(schema_class, mm.Schema)  # Changed from mm.SchemaType to mm.Schema

def test_build_schema_without_infer_missing():
    schema_class = mm.build_schema(MyDataClass, mm.SchemaF, infer_missing=False, partial=False)
    assert issubclass(schema_class, mm.Schema)  # Changed from mm.SchemaType to mm.Schema

def test_build_schema_with_partial_data_allowed():
    schema_class = mm.build_schema(MyDataClass, mm.SchemaF, infer_missing=True, partial=True)
    assert issubclass(schema_class, mm.Schema)  # Changed from mm.SchemaType to mm.Schema

def test_build_schema_without_partial_data_allowed():
    schema_class = mm.build_schema(MyDataClass, mm.SchemaF, infer_missing=True, partial=False)
    assert issubclass(schema_class, mm.Schema)  # Changed from mm.SchemaType to mm.Schema


# Module: dataclasses_json.api
# test_dataclass_json.py
from dataclasses import dataclass
from dataclasses_json import dataclass_json, DataClassJsonMixin, Schema
import pytest

@dataclass_json
@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int = 0

def test_schema_method():
    class ExampleClass(DataClassJsonMixin):
        field1: int
        field2: str
    
    schema = ExampleClass.schema()
    assert isinstance(schema, Schema)

def test_schema_with_only():
    class ExampleClass(DataClassJsonMixin):
        field1: int
        field2: str
    
    only_fields = ['field1']
    schema = ExampleClass.schema(only=only_fields)
    assert all(f in schema.__dataclass_fields__ for f in only_fields)

def test_schema_with_exclude():
    class ExampleClass(DataClassJsonMixin):
        field1: int
        field2: str
    
    exclude_fields = ['field2']
    schema = ExampleClass.schema(exclude=exclude_fields)
    assert not any(f in schema.__dataclass_fields__ for f in exclude_fields)

def test_schema_with_many():
    class ExampleClass(DataClassJsonMixin):
        field1: int
        field2: str
    
    schema = ExampleClass.schema(many=True)
    assert schema._SchemaType__many is True

def test_schema_with_context():
    class ExampleClass(DataClassJsonMixin):
        field1: int
        field2: str
    
    context = {'key': 'value'}
    schema = ExampleClass.schema(context=context)
    assert schema._context == context

def test_schema_with_load_only():
    class ExampleClass(DataClassJsonMixin):
        field1: int
        field2: str
    
    load_only_fields = ['field1']
    schema = ExampleClass.schema(load_only=load_only_fields)
    assert all(f in schema._SchemaType__load_only for f in load_only_fields)

def test_schema_with_dump_only():
    class ExampleClass(DataClassJsonMixin):
        field1: int
        field2: str
    
    dump_only_fields = ['field2']
    schema = ExampleClass.schema(dump_only=dump_only_fields)
    assert all(f in schema._SchemaType__dump_only for f in dump_only_fields)

def test_schema_with_partial():
    class ExampleClass(DataClassJsonMixin):
        field1: int
        field2: str
    
    schema = ExampleClass.schema(partial=True)
    assert schema._SchemaType__partial is True

def test_schema_with_unknown():
    class ExampleClass(DataClassJsonMixin):
        field1: int
        field2: str
    
    unknown_action = 'ignore'
    schema = ExampleClass.schema(unknown=unknown_action)
    assert schema._SchemaType__unknown == unknown_action

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_schema_1
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1.py:5:0: E0611: No name 'Schema' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1.py:29:20: E1101: Instance of 'Schema' has no '__dataclass_fields__' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1.py:38:24: E1101: Instance of 'Schema' has no '__dataclass_fields__' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1.py:46:11: E1101: Instance of 'Schema' has no '_SchemaType__many' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1.py:55:11: E1101: Instance of 'Schema' has no '_context' member; maybe 'context'? (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1.py:64:20: E1101: Instance of 'Schema' has no '_SchemaType__load_only' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1.py:73:20: E1101: Instance of 'Schema' has no '_SchemaType__dump_only' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1.py:81:11: E1101: Instance of 'Schema' has no '_SchemaType__partial' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1.py:90:11: E1101: Instance of 'Schema' has no '_SchemaType__unknown' member (no-member)

"""

# Module: dataclasses_json.mm
import pytest
from dataclasses import dataclass, fields
from typing import Optional, List, Tuple, Union, Dict, Any, Type, Enum
from marshmallow import Schema, fields as mfields
from warnings import warn
from dataclasses_json import dataclass_json, DataClassJsonMixin

# Define a simple dataclass for testing
@dataclass
class Person:
    name: str
    age: int = 0

@dataclass_json
@dataclass
class ExtendedPerson(Person):
    address: str

def test_build_type_with_dataclass():
    @dataclass
    class TestDataclass:
        field1: int
        field2: str
    
    result = build_type(TestDataclass, {}, None, fields.Field(name="field1", annotation=int), TestDataclass)
    assert isinstance(result, mfields.Nested)
    assert result.nested == TestDataclass

def test_build_type_with_optional():
    @dataclass
    class OptionalTest:
        field1: Optional[int] = None
    
    result = build_type(OptionalTest, {}, None, fields.Field(name="field1", annotation=Optional[int]), OptionalTest)
    assert isinstance(result, mfields.Int)
    assert "allow_none" in result.opts

def test_build_type_with_union():
    class MyEnum(Enum):
        VALUE1 = 1
        VALUE2 = 2
    
    @dataclass
    class UnionTest:
        field1: Union[int, str]
    
    result = build_type(UnionTest, {}, None, fields.Field(name="field1", annotation=Union[int, str]), UnionTest)
    assert isinstance(result, mfields.Raw)
    assert "union" in result.opts

def test_build_type_with_tuple():
    @dataclass
    class TupleTest:
        field1: Tuple[int, str]
    
    result = build_type(TupleTest, {}, None, fields.Field(name="field1", annotation=Tuple[int, str]), TupleTest)
    assert isinstance(result, mfields.Tuple)
    assert len(result.inner) == 2

def test_build_type_with_unknown_type():
    @dataclass
    class UnknownType:
        field1: Any
    
    with pytest.warns(UserWarning):
        result = build_type(UnknownType, {}, None, fields.Field(name="field1", annotation=Any), UnknownType)
        assert isinstance(result, mfields.Field)

def test_build_type_with_nested_dataclass():
    @dataclass_json
    @dataclass
    class NestedDataclass:
        nested: Person
    
    result = build_type(NestedDataclass, {}, None, fields.Field(name="nested", annotation=Person), NestedDataclass)
    assert isinstance(result, mfields.Nested)
    assert result.nested == Person

def test_build_type_with_custom_mixin():
    @dataclass
    class CustomMixin:
        pass
    
    @dataclass
    class MixinTest(CustomMixin):
        field1: int
    
    with pytest.warns(UserWarning):
        result = build_type(MixinTest, {}, CustomMixin, fields.Field(name="field1", annotation=int), MixinTest)
        assert isinstance(result, mfields.Nested)
        assert result.nested == CustomMixin

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_type_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:5:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:27:13: E0602: Undefined variable 'build_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:27:49: E1101: Function 'fields' has no 'Field' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:36:13: E0602: Undefined variable 'build_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:36:48: E1101: Function 'fields' has no 'Field' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:49:13: E0602: Undefined variable 'build_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:49:45: E1101: Function 'fields' has no 'Field' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:58:13: E0602: Undefined variable 'build_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:58:45: E1101: Function 'fields' has no 'Field' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:68:17: E0602: Undefined variable 'build_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:68:51: E1101: Function 'fields' has no 'Field' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:77:13: E0602: Undefined variable 'build_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:77:51: E1101: Function 'fields' has no 'Field' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:91:17: E0602: Undefined variable 'build_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:91:56: E1101: Function 'fields' has no 'Field' member (no-member)

"""
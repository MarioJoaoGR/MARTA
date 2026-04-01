
import pytest
from marshmallow import fields
from dataclasses import dataclass, make_dataclass
from typing import Optional, Tuple, Union
from dataclasses_json.mm import build_type

# Define a simple dataclass for testing
@dataclass
class TestDataClass:
    name: str
    age: int

def test_build_type_with_dataclass():
    field = make_dataclass('TestField', [('name', Optional[str])])(name='name')
    built_field = build_type(TestDataClass, {}, None, field, TestDataClass)
    assert isinstance(built_field, fields.Nested)
    assert built_field.nested == TestDataClass.__annotations__['age']

def test_build_type_with_optional():
    @dataclass
    class OptionalTestDataClass:
        name: Optional[str] = None
    
    field = make_dataclass('OptionalField', [('name', Optional[str])])(name='name')
    built_field = build_type(OptionalTestDataClass, {}, None, field, OptionalTestDataClass)
    assert isinstance(built_field, fields.Nested)
    assert built_field.nested == OptionalTestDataClass.__annotations__['name']

def test_build_type_with_tuple():
    @dataclass
    class TupleTestDataClass:
        names: Tuple[str, ...]
    
    field = make_dataclass('TupleField', [('names', Tuple[str, ...])])(name='names')
    built_field = build_type(TupleTestDataClass, {}, None, field, TupleTestDataClass)
    assert isinstance(built_field, fields.Tuple)
    assert built_field.items == TupleTestDataClass.__annotations__['names']

def test_build_type_with_union():
    @dataclass
    class UnionTestDataClass:
        name: Union[str, int]
    
    field = make_dataclass('UnionField', [('name', Union[str, int])])(name='name')
    built_field = build_type(UnionTestDataClass, {}, None, field, UnionTestDataClass)
    assert isinstance(built_field, fields.Raw)  # Assuming _UnionField returns Raw in this context
    assert built_field.data_key == 'name'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_build_type_with_dataclass ________________________

    def test_build_type_with_dataclass():
        field = make_dataclass('TestField', [('name', Optional[str])])(name='name')
>       built_field = build_type(TestDataClass, {}, None, field, TestDataClass)

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/mm.py:293: in build_type
    return inner(type_, options)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = <class 'Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_valid_inputs.TestDataClass'>
options = {}

    def inner(type_, options):
        while True:
            if not _is_new_type(type_):
                break
    
            type_ = type_.__supertype__
    
        if is_dataclass(type_):
            if _issubclass_safe(type_, mixin):
                options['field_many'] = bool(
                    _is_supported_generic(field.type) and _is_collection(
                        field.type))
                return fields.Nested(type_.schema(), **options)
            else:
                warnings.warn(f"Nested dataclass field {field.name} of type "
>                             f"{field.type} detected in "
                              f"{cls.__name__} that is not an instance of "
                              f"dataclass_json. Did you mean to recursively "
                              f"serialize this field? If so, make sure to "
                              f"augment {type_} with either the "
                              f"`dataclass_json` decorator or mixin.")
E               AttributeError: 'TestField' object has no attribute 'type'

dataclasses-json/dataclasses_json/mm.py:254: AttributeError
________________________ test_build_type_with_optional _________________________

    def test_build_type_with_optional():
        @dataclass
        class OptionalTestDataClass:
            name: Optional[str] = None
    
        field = make_dataclass('OptionalField', [('name', Optional[str])])(name='name')
>       built_field = build_type(OptionalTestDataClass, {}, None, field, OptionalTestDataClass)

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/mm.py:293: in build_type
    return inner(type_, options)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = <class 'Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_valid_inputs.test_build_type_with_optional.<locals>.OptionalTestDataClass'>
options = {}

    def inner(type_, options):
        while True:
            if not _is_new_type(type_):
                break
    
            type_ = type_.__supertype__
    
        if is_dataclass(type_):
            if _issubclass_safe(type_, mixin):
                options['field_many'] = bool(
                    _is_supported_generic(field.type) and _is_collection(
                        field.type))
                return fields.Nested(type_.schema(), **options)
            else:
                warnings.warn(f"Nested dataclass field {field.name} of type "
>                             f"{field.type} detected in "
                              f"{cls.__name__} that is not an instance of "
                              f"dataclass_json. Did you mean to recursively "
                              f"serialize this field? If so, make sure to "
                              f"augment {type_} with either the "
                              f"`dataclass_json` decorator or mixin.")
E               AttributeError: 'OptionalField' object has no attribute 'type'

dataclasses-json/dataclasses_json/mm.py:254: AttributeError
__________________________ test_build_type_with_tuple __________________________

    def test_build_type_with_tuple():
        @dataclass
        class TupleTestDataClass:
            names: Tuple[str, ...]
    
>       field = make_dataclass('TupleField', [('names', Tuple[str, ...])])(name='names')
E       TypeError: TupleField.__init__() got an unexpected keyword argument 'name'

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:35: TypeError
__________________________ test_build_type_with_union __________________________

    def test_build_type_with_union():
        @dataclass
        class UnionTestDataClass:
            name: Union[str, int]
    
        field = make_dataclass('UnionField', [('name', Union[str, int])])(name='name')
>       built_field = build_type(UnionTestDataClass, {}, None, field, UnionTestDataClass)

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:46: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/mm.py:293: in build_type
    return inner(type_, options)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = <class 'Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_valid_inputs.test_build_type_with_union.<locals>.UnionTestDataClass'>
options = {}

    def inner(type_, options):
        while True:
            if not _is_new_type(type_):
                break
    
            type_ = type_.__supertype__
    
        if is_dataclass(type_):
            if _issubclass_safe(type_, mixin):
                options['field_many'] = bool(
                    _is_supported_generic(field.type) and _is_collection(
                        field.type))
                return fields.Nested(type_.schema(), **options)
            else:
                warnings.warn(f"Nested dataclass field {field.name} of type "
>                             f"{field.type} detected in "
                              f"{cls.__name__} that is not an instance of "
                              f"dataclass_json. Did you mean to recursively "
                              f"serialize this field? If so, make sure to "
                              f"augment {type_} with either the "
                              f"`dataclass_json` decorator or mixin.")
E               AttributeError: 'UnionField' object has no attribute 'type'

dataclasses-json/dataclasses_json/mm.py:254: AttributeError
=============================== warnings summary ===============================
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:9
  /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py:9: PytestCollectionWarning: cannot collect test class 'TestDataClass' because it has a __init__ constructor (from: Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py)
    @dataclass

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py::test_build_type_with_dataclass
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py::test_build_type_with_optional
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py::test_build_type_with_tuple
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_inputs.py::test_build_type_with_union
========================= 4 failed, 1 warning in 0.07s =========================
"""
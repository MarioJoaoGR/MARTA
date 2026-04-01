
import pytest
from dataclasses_json.mm import _UnionField, is_dataclass, _get_type_origin
from dataclasses import dataclass
from typing import Union

@dataclass
class DataClass1:
    field1: int

@dataclass
class DataClass2:
    field2: str

desc = {DataClass1: lambda v, a, d, **k: DataClass1(**v), DataClass2: lambda v, a, d, **k: DataClass2(**v)}

def test_invalid_input():
    union_field = _UnionField(desc, None, None)
    
    # Test case for invalid input (non-dict type without '__type' field)
    value = "not a dict"
    with pytest.warns(UserWarning):
        deserialized_value = union_field._deserialize(value, 'field', {})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        union_field = _UnionField(desc, None, None)
    
        # Test case for invalid input (non-dict type without '__type' field)
        value = "not a dict"
        with pytest.warns(UserWarning):
>           deserialized_value = union_field._deserialize(value, 'field', {})

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_invalid_input.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <fields._UnionField(dump_default=<marshmallow.missing>, attribute=None, validate=None, required=False, load_only=False...equired': 'Missing data for required field.', 'null': 'Field may not be null.', 'validator_failed': 'Invalid value.'})>
value = 'not a dict', attr = 'field', data = {}, kwargs = {}
tmp_value = 'not a dict'
type_ = <class 'Test4DT_tests.test_dataclasses_json_mm__UnionField__deserialize_0_test_invalid_input.DataClass2'>
schema_ = <function <lambda> at 0x101aacd30>

    def _deserialize(self, value, attr, data, **kwargs):
        tmp_value = deepcopy(value)
        if isinstance(tmp_value, dict) and '__type' in tmp_value:
            dc_name = tmp_value['__type']
            for type_, schema_ in self.desc.items():
                if is_dataclass(type_) and type_.__name__ == dc_name:
                    del tmp_value['__type']
                    return schema_._deserialize(tmp_value, attr, data, **kwargs)
        elif isinstance(tmp_value, dict):
            warnings.warn(
                f'Attempting to deserialize "dict" (value: "{tmp_value}) '
                f'that does not have a "__type" type specifier field into'
                f'(dataclass: {self.cls.__name__}, field: {self.field.name}).'
                f'Deserialization may fail, or deserialization to wrong type may occur.'
            )
            return super()._deserialize(tmp_value, attr, data, **kwargs)
        else:
            for type_, schema_ in self.desc.items():
                if isinstance(tmp_value, _get_type_origin(type_)):
                    return schema_._deserialize(tmp_value, attr, data, **kwargs)
            else:
                warnings.warn(
                    f'The type "{type(tmp_value).__name__}" (value: "{tmp_value}") '
                    f'is not in the list of possible types of typing.Union '
>                   f'(dataclass: {self.cls.__name__}, field: {self.field.name}). '
                    f'Value cannot be deserialized properly.')
E               AttributeError: 'NoneType' object has no attribute '__name__'. Did you mean: '__ne__'?

dataclasses-json/dataclasses_json/mm.py:119: AttributeError

During handling of the above exception, another exception occurred:

    def test_invalid_input():
        union_field = _UnionField(desc, None, None)
    
        # Test case for invalid input (non-dict type without '__type' field)
        value = "not a dict"
>       with pytest.warns(UserWarning):
E       Failed: DID NOT WARN. No warnings of type (<class 'UserWarning'>,) were emitted.
E        Emitted warnings: [].

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_invalid_input.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""

import pytest
from dataclasses import dataclass, fields
from typing import Union
from copy import deepcopy
import warnings
from dataclasses_json.mm import _UnionField, is_dataclass, _get_type_origin

@pytest.mark.parametrize("value, expected", [
    ({'__type': 'int', 'value': 123}, 123),
    ({'__type': 'str', 'value': 'test'}, 'test'),
    ({'value': 123}, None)  # This should trigger a warning
])
def test_deserialize(value, expected):
    @dataclass
    class Example:
        field: Union[int, str]
    
    desc = {Example: lambda v, a, d: None}
    union_field = _UnionField(desc, Example, fields(Example)[0])
    
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.warns(expected):
            assert union_field._deserialize(value, 'field', {'field': value}) == expected
    else:
        result = union_field._deserialize(value, 'field', {'field': value})
        assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_deserialize[value0-123] _________________________

value = {'__type': 'int', 'value': 123}, expected = 123

    @pytest.mark.parametrize("value, expected", [
        ({'__type': 'int', 'value': 123}, 123),
        ({'__type': 'str', 'value': 'test'}, 'test'),
        ({'value': 123}, None)  # This should trigger a warning
    ])
    def test_deserialize(value, expected):
        @dataclass
        class Example:
            field: Union[int, str]
    
        desc = {Example: lambda v, a, d: None}
        union_field = _UnionField(desc, Example, fields(Example)[0])
    
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.warns(expected):
                assert union_field._deserialize(value, 'field', {'field': value}) == expected
        else:
            result = union_field._deserialize(value, 'field', {'field': value})
>           assert result == expected
E           assert None == 123

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py:27: AssertionError
________________________ test_deserialize[value1-test] _________________________

value = {'__type': 'str', 'value': 'test'}, expected = 'test'

    @pytest.mark.parametrize("value, expected", [
        ({'__type': 'int', 'value': 123}, 123),
        ({'__type': 'str', 'value': 'test'}, 'test'),
        ({'value': 123}, None)  # This should trigger a warning
    ])
    def test_deserialize(value, expected):
        @dataclass
        class Example:
            field: Union[int, str]
    
        desc = {Example: lambda v, a, d: None}
        union_field = _UnionField(desc, Example, fields(Example)[0])
    
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.warns(expected):
                assert union_field._deserialize(value, 'field', {'field': value}) == expected
        else:
            result = union_field._deserialize(value, 'field', {'field': value})
>           assert result == expected
E           AssertionError: assert None == 'test'

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py:27: AssertionError
________________________ test_deserialize[value2-None] _________________________

value = {'value': 123}, expected = None

    @pytest.mark.parametrize("value, expected", [
        ({'__type': 'int', 'value': 123}, 123),
        ({'__type': 'str', 'value': 'test'}, 'test'),
        ({'value': 123}, None)  # This should trigger a warning
    ])
    def test_deserialize(value, expected):
        @dataclass
        class Example:
            field: Union[int, str]
    
        desc = {Example: lambda v, a, d: None}
        union_field = _UnionField(desc, Example, fields(Example)[0])
    
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.warns(expected):
                assert union_field._deserialize(value, 'field', {'field': value}) == expected
        else:
            result = union_field._deserialize(value, 'field', {'field': value})
>           assert result == expected
E           AssertionError: assert {'value': 123} == None

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py:27: AssertionError
=============================== warnings summary ===============================
Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py::test_deserialize[value2-None]
  /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/dataclasses_json/mm.py:104: UserWarning: Attempting to deserialize "dict" (value: "{'value': 123}) that does not have a "__type" type specifier field into(dataclass: Example, field: field).Deserialization may fail, or deserialization to wrong type may occur.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py::test_deserialize[value0-123]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py::test_deserialize[value1-test]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py::test_deserialize[value2-None]
========================= 3 failed, 1 warning in 0.06s =========================
"""
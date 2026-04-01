
import pytest
from dataclasses import dataclass
from typing import Union
from dataclasses_json.mm import _UnionField

@dataclass
class DataClass1:
    field1: int

@dataclass
class DataClass2:
    field2: str

# Define the fixture for _UnionField
@pytest.fixture(name="_UnionField")
def union_field_fixture():
    desc = {DataClass1: lambda v, a, d, **k: DataClass1(**v), DataClass2: lambda v, a, d, **k: DataClass2(**v)}
    return _UnionField(desc, None, None)

# Use the fixture in your tests
@pytest.mark.parametrize("value, expected", [
    ({'__type': 'DataClass1', '__value__': {'field1': 1}}, DataClass1(field1=1)),
    ({'__type': 'DataClass2', '__value__': {'field2': 'test'}}, DataClass2(field2='test')),
    ({'field1': 1}, DataClass1(field1=1))
])
def test_deserialize_edge_case(_UnionField, value, expected):
    assert _UnionField._deserialize(value) == expected

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
_________________ test_deserialize_edge_case[value0-expected0] _________________

_UnionField = <fields._UnionField(dump_default=<marshmallow.missing>, attribute=None, validate=None, required=False, load_only=False...equired': 'Missing data for required field.', 'null': 'Field may not be null.', 'validator_failed': 'Invalid value.'})>
value = {'__type': 'DataClass1', '__value__': {'field1': 1}}
expected = DataClass1(field1=1)

    @pytest.mark.parametrize("value, expected", [
        ({'__type': 'DataClass1', '__value__': {'field1': 1}}, DataClass1(field1=1)),
        ({'__type': 'DataClass2', '__value__': {'field2': 'test'}}, DataClass2(field2='test')),
        ({'field1': 1}, DataClass1(field1=1))
    ])
    def test_deserialize_edge_case(_UnionField, value, expected):
>       assert _UnionField._deserialize(value) == expected
E       TypeError: _UnionField._deserialize() missing 2 required positional arguments: 'attr' and 'data'

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py:28: TypeError
_________________ test_deserialize_edge_case[value1-expected1] _________________

_UnionField = <fields._UnionField(dump_default=<marshmallow.missing>, attribute=None, validate=None, required=False, load_only=False...equired': 'Missing data for required field.', 'null': 'Field may not be null.', 'validator_failed': 'Invalid value.'})>
value = {'__type': 'DataClass2', '__value__': {'field2': 'test'}}
expected = DataClass2(field2='test')

    @pytest.mark.parametrize("value, expected", [
        ({'__type': 'DataClass1', '__value__': {'field1': 1}}, DataClass1(field1=1)),
        ({'__type': 'DataClass2', '__value__': {'field2': 'test'}}, DataClass2(field2='test')),
        ({'field1': 1}, DataClass1(field1=1))
    ])
    def test_deserialize_edge_case(_UnionField, value, expected):
>       assert _UnionField._deserialize(value) == expected
E       TypeError: _UnionField._deserialize() missing 2 required positional arguments: 'attr' and 'data'

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py:28: TypeError
_________________ test_deserialize_edge_case[value2-expected2] _________________

_UnionField = <fields._UnionField(dump_default=<marshmallow.missing>, attribute=None, validate=None, required=False, load_only=False...equired': 'Missing data for required field.', 'null': 'Field may not be null.', 'validator_failed': 'Invalid value.'})>
value = {'field1': 1}, expected = DataClass1(field1=1)

    @pytest.mark.parametrize("value, expected", [
        ({'__type': 'DataClass1', '__value__': {'field1': 1}}, DataClass1(field1=1)),
        ({'__type': 'DataClass2', '__value__': {'field2': 'test'}}, DataClass2(field2='test')),
        ({'field1': 1}, DataClass1(field1=1))
    ])
    def test_deserialize_edge_case(_UnionField, value, expected):
>       assert _UnionField._deserialize(value) == expected
E       TypeError: _UnionField._deserialize() missing 2 required positional arguments: 'attr' and 'data'

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py:28: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py::test_deserialize_edge_case[value0-expected0]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py::test_deserialize_edge_case[value1-expected1]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_edge_case.py::test_deserialize_edge_case[value2-expected2]
============================== 3 failed in 0.04s ===============================
"""
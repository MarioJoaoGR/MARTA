
import pytest
from unittest.mock import patch, MagicMock
from typesystem.json_schema import type_from_json_schema, SchemaDefinitions
from typesystem import Field, Union, Const, NeverMatch

# Test 1: Building a number field with constraints from JSON schema data
def test_type_from_json_schema_number():
    data = {"type": "number", "minimum": 0, "maximum": 10}
    definitions = SchemaDefinitions()
    result = type_from_json_schema(data, definitions)
    assert isinstance(result, Field)
    assert result.type == 'number'
    assert result.constraints['minimum'] == 0
    assert result.constraints['maximum'] == 10

# Test 2: Building an object field with specified properties and required fields
def test_type_from_json_schema_object():
    data = {"type": "object", "properties": {"name": {"type": "string"}, "age": {"type": "integer"}}, "required": ["name"]}
    definitions = SchemaDefinitions()
    result = type_from_json_schema(data, definitions)
    assert isinstance(result, Field)
    assert result.type == 'object'
    assert len(result.properties) == 2
    assert 'name' in result.properties and isinstance(result.properties['name'], Field)
    assert 'age' in result.properties and isinstance(result.properties['age'], Field)
    assert 'name' in result.required_fields

# Test 3: Building a union of possible types from JSON schema data
def test_type_from_json_schema_union():
    data = {"type": ["null", "number"]}
    definitions = SchemaDefinitions()
    with patch('typesystem.json_schema.get_valid_types', return_value=(["null", "number"], True)):
        result = type_from_json_schema(data, definitions)
    assert isinstance(result, Union)
    assert len(result.any_of) == 2
    assert any(isinstance(item, Field) and item.type == 'number' for item in result.any_of)
    assert any(isinstance(item, Const) and item.value is None for item in result.any_of)
    assert result.allow_null

# Test 4: Handling no valid types by returning NeverMatch when allow_null is False
def test_type_from_json_schema_no_valid_types():
    data = {"type": []}
    definitions = SchemaDefinitions()
    with patch('typesystem.json_schema.get_valid_types', return_value=([], False)):
        result = type_from_json_schema(data, definitions)
    assert isinstance(result, NeverMatch)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___ ERROR collecting test_typesystem_json_schema_type_from_json_schema_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_type_from_json_schema_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_type_from_json_schema_0.py:5: in <module>
    from typesystem import Field, Union, Const, NeverMatch
E   ImportError: cannot import name 'Const' from 'typesystem' (/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_type_from_json_schema_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.20s ===============================
"""
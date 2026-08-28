
import pytest
from unittest.mock import patch, MagicMock
from typesystem.json_schema import all_of_from_json_schema, NO_DEFAULT
from typesystem import Field, SchemaDefinitions, AllOf

# Scenario 1: Basic Usage
def test_all_of_from_json_schema_basic():
    data = {
        "allOf": [{"type": "string"}, {"minimum": 10}],
        "default": None
    }
    definitions = {}
    
    with patch('typesystem.json_schema.from_json_schema', side_effect=lambda x, d: Field(**x)):
        result = all_of_from_json_schema(data, definitions)
        
    assert isinstance(result, AllOf)
    assert len(result.all_of) == 2
    assert all(isinstance(f, Field) for f in result.all_of)
    assert result.default is None

# Scenario 2: Providing Definitions
def test_all_of_from_json_schema_with_definitions():
    data = {
        "allOf": [{"type": "string"}, {"minimum": 10}],
        "default": None
    }
    definitions = {
        "StringSchema": Field(type="string"),
        "NumberSchema": Field(type="number", minimum=10)
    }
    
    with patch('typesystem.json_schema.from_json_schema', side_effect=lambda x, d: Field(**x)):
        result = all_of_from_json_schema(data, definitions)
        
    assert isinstance(result, AllOf)
    assert len(result.all_of) == 2
    assert all(isinstance(f, Field) for f in result.all_of)
    assert result.default is None

# Scenario 3: Default Value Handling
def test_all_of_from_json_schema_default_value():
    data = {
        "allOf": [{"type": "string"}, {"minimum": 10}],
    }
    definitions = {}
    
    with patch('typesystem.json_schema.from_json_schema', side_effect=lambda x, d: Field(**x)):
        result = all_of_from_json_schema(data, definitions)
        
    assert isinstance(result, AllOf)
    assert len(result.all_of) == 2
    assert all(isinstance(f, Field) for f in result.all_of)
    assert result.default is NO_DEFAULT

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
__ ERROR collecting test_typesystem_json_schema_all_of_from_json_schema_0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_all_of_from_json_schema_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_all_of_from_json_schema_0.py:5: in <module>
    from typesystem import Field, SchemaDefinitions, AllOf
E   ImportError: cannot import name 'AllOf' from 'typesystem' (/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_all_of_from_json_schema_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.28s ===============================
"""
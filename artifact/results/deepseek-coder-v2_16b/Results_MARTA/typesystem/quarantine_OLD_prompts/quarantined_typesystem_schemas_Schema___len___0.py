
import pytest
from typesystem.schemas import SchemaExample, Field

# Test initialization with a dictionary as positional argument
def test_schema_initialization_with_dict():
    schema = SchemaExample({'name': 'Alice', 'age': 30})
    assert hasattr(schema, 'name') and schema.name == 'Alice'
    assert hasattr(schema, 'age') and schema.age == 30

# Test initialization with keyword arguments only
def test_schema_initialization_with_kwargs():
    schema = SchemaExample(name='Bob', age=25)
    assert hasattr(schema, 'name') and schema.name == 'Bob'
    assert hasattr(schema, 'age') and schema.age == 30  # Default value used for age

# Test initialization with an invalid keyword argument
def test_schema_initialization_with_invalid_kwarg():
    with pytest.raises(TypeError):
        SchemaExample(invalid_arg='Invalid')

# Test the __len__ method to check the number of fields
def test_schema_length():
    schema = SchemaExample({'name': 'Alice', 'age': 30})
    assert len(schema) == 2

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
_________ ERROR collecting test_typesystem_schemas_Schema___len___0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_schemas_Schema___len___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_schemas_Schema___len___0.py:3: in <module>
    from typesystem.schemas import SchemaExample, Field
E   ImportError: cannot import name 'SchemaExample' from 'typesystem.schemas' (/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/schemas.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_schemas_Schema___len___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.20s ===============================
"""
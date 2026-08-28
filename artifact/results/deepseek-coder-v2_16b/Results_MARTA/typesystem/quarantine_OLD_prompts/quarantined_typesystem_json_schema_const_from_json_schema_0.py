
import pytest
from unittest.mock import patch, MagicMock
from typesystem.json_schema import const_from_json_schema, NO_DEFAULT
from typesystem import Field, Const

# Test 1: Basic Call with Minimal Data
def test_const_from_json_schema_basic():
    data = {"const": 42}
    definitions = MagicMock()
    result = const_from_json_schema(data, definitions)
    assert isinstance(result, Const)
    assert result.const == 42
    assert result.default == NO_DEFAULT

# Test 2: Call with Default Value Present
def test_const_from_json_schema_with_default():
    data = {"const": 42, "default": None}
    definitions = MagicMock()
    with pytest.raises(AssertionError) as e:
        const_from_json_schema(data, definitions)
    assert str(e.value) == f"Must be the value '{42}'."

# Test 3: Call with No Default Value Present
def test_const_from_json_schema_no_default():
    data = {"const": 42}
    definitions = MagicMock()
    result = const_from_json_schema(data, definitions)
    assert isinstance(result, Const)
    assert result.const == 42
    assert result.default == NO_DEFAULT

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
___ ERROR collecting test_typesystem_json_schema_const_from_json_schema_0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_const_from_json_schema_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_const_from_json_schema_0.py:5: in <module>
    from typesystem import Field, Const
E   ImportError: cannot import name 'Const' from 'typesystem' (/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_const_from_json_schema_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.22s ===============================
"""
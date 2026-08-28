
import pytest
from dataclasses_json.undefined import handle_from_dict, UndefinedParameterError
from typing import Dict, Any, Optional
import dataclasses

# Define a simple dataclass with a catch-all field
@dataclasses.dataclass
class MyDataClass:
    a: int = 0
    b: str = "default"
    catch_all: Optional[Dict] = None

def test_handle_from_dict_with_defined_and_undefined_parameters():
    kvs = {'a': 1, 'b': 'value', 'c': 3}
    result = handle_from_dict(MyDataClass, kvs)
    assert 'catch_all' in result
    assert result['catch_all'] == {'c': 3}

def test_handle_from_dict_with_no_undefined_parameters():
    kvs = {'a': 1, 'b': 'value'}
    result = handle_from_dict(MyDataClass, kvs)
    assert 'catch_all' not in result
    assert result['catch_all'] == {}

def test_handle_from_dict_with_parameter_name_same_as_catch_all():
    kvs = {'a': 1, 'b': 'value', 'catch_all': 'unexpected'}
    with pytest.raises(UndefinedParameterError) as excinfo:
        handle_from_dict(MyDataClass, kvs)
    assert str(excinfo.value) == "Received input field with same name as catch-all field: 'catch_all': 'unexpected'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0.py:3: in <module>
    from dataclasses_json.undefined import handle_from_dict, UndefinedParameterError
E   ImportError: cannot import name 'handle_from_dict' from 'dataclasses_json.undefined' (/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""

import pytest
from dataclasses_json.core import _is_supported_generic
from typing import Optional, List, Enum

# Test scenario 1: Check if a non-string type that is not an enum or collection raises False
def test_is_supported_generic_non_str_not_enum_or_collection():
    class MyCustomType:
        pass
    
    assert _is_supported_generic(MyCustomType) == False

# Test scenario 2: Check if an optional type raises True
def test_is_supported_generic_optional_type():
    assert _is_supported_generic(Optional[int]) == True

# Test scenario 3: Check if a list type raises False
def test_is_supported_generic_list_type():
    assert _is_supported_generic(List[str]) == False

# Test scenario 4: Check if an enum type raises True
class MyEnum(Enum):
    A = 1
    B = 2

def test_is_supported_generic_enum_type():
    assert _is_supported_generic(MyEnum) == True

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
____ ERROR collecting test_dataclasses_json_core__is_supported_generic_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__is_supported_generic_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__is_supported_generic_0.py:4: in <module>
    from typing import Optional, List, Enum
E   ImportError: cannot import name 'Enum' from 'typing' (/opt/conda/envs/test4py_env/lib/python3.10/typing.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__is_supported_generic_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""
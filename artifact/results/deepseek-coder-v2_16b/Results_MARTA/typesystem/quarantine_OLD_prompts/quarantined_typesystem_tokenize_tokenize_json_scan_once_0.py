
import pytest
from typesystem.tokenize.tokenize_json import scan_once

def test_scan_once_empty_object():
    result = scan_once("{}", 0)
    assert result == (Token(type='BEGIN_OBJECT', value={}), 0)

def test_scan_once_complex_object():
    result = scan_once('{"key": "value", "list": [1, 2, 3]}', 0)
    assert result == (Token(type='BEGIN_OBJECT', value={"key": "value", "list": [1, 2, 3]}), 0)

def test_scan_once_specific_index():
    result = scan_once('{ "key": "value", "list": [1, 2, 3] }', 5)
    assert result == (Token(type='BEGIN_OBJECT', value={"key": "value", "list": [1, 2, 3]}), 5)

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
____ ERROR collecting test_typesystem_tokenize_tokenize_json_scan_once_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_json_scan_once_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_json_scan_once_0.py:3: in <module>
    from typesystem.tokenize.tokenize_json import scan_once
E   ImportError: cannot import name 'scan_once' from 'typesystem.tokenize.tokenize_json' (/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/tokenize/tokenize_json.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_json_scan_once_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.19s ===============================
"""
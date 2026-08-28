
import pytest
from typesystem.tokenize.tokens import NestedKey

# Scenario 1: Test standard input with valid schema definitions
def test_valid_inputs():
    nested_dict = {
        "key1": {"nestedKey1": NestedKey({"finalKey": "value"}), "nestedKey2": NestedKey({"anotherFinalKey": "anotherValue"})},
        "key2": {"nestedKey3": NestedKey({"yetAnotherKey": "yetAnotherValue"})}
    }
    
    nested_instance = NestedKey(nested_dict)
    
    assert isinstance(nested_instance, NestedKey), "Instance should be an instance of NestedKey"
    assert len(nested_instance._child_keys) == 2, "There should be 2 child keys in _child_keys dictionary"
    assert len(nested_instance._child_tokens) == 2, "There should be 2 child tokens in _child_tokens dictionary"
    
    # Check the existence of specific child keys and tokens
    assert "key1" in nested_instance._child_keys, "_child_keys should contain 'key1'"
    assert "nestedKey1" in nested_instance._child_keys["key1"], "_child_keys['key1'] should contain 'nestedKey1'"
    assert "anotherFinalKey" in nested_instance._child_tokens["key2"]["nestedKey3"], "_child_tokens['key2']['nestedKey3'] should contain 'anotherFinalKey'"

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
___ ERROR collecting test_typesystem_tokenize_tokens_DictToken___init___0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokens_DictToken___init___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokens_DictToken___init___0.py:3: in <module>
    from typesystem.tokenize.tokens import NestedKey
E   ImportError: cannot import name 'NestedKey' from 'typesystem.tokenize.tokens' (/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/tokenize/tokens.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokens_DictToken___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.18s ===============================
"""
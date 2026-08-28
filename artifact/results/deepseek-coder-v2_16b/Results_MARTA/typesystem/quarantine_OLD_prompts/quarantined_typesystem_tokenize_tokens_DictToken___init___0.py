
import pytest
from typesystem.tokenize.tokens import NestedKey  # Assuming the module path for NestedKey

def test_nestedkey_init():
    nested_dict = {
        "key1": {"nestedKey1": NestedKey({"finalKey": "value"}), "nestedKey2": NestedKey({"anotherFinalKey": "anotherValue"})},
        "key2": {"nestedKey3": NestedKey({"yetAnotherKey": "yetAnotherValue"})}
    }
    
    nested_instance = NestedKey(nested_dict)
    
    assert isinstance(nested_instance, NestedKey), "Instance should be an instance of NestedKey"
    assert len(nested_instance._child_keys) == 2, "_child_keys should contain 2 items"
    assert len(nested_instance._child_tokens) == 2, "_child_tokens should contain 2 items"
    
    # Additional assertions to check the structure of nested keys and tokens
    assert "key1" in nested_instance._child_keys, "'key1' should be a child key in _child_keys"
    assert "nestedKey1" in nested_instance._child_tokens, "'nestedKey1' should be a child token in _child_tokens"
    assert "key2" in nested_instance._child_keys, "'key2' should be a child key in _child_keys"
    assert "nestedKey3" in nested_instance._child_tokens, "'nestedKey3' should be a child token in _child_tokens"

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
    from typesystem.tokenize.tokens import NestedKey  # Assuming the module path for NestedKey
E   ImportError: cannot import name 'NestedKey' from 'typesystem.tokenize.tokens' (/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/tokenize/tokens.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokens_DictToken___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.20s ===============================
"""
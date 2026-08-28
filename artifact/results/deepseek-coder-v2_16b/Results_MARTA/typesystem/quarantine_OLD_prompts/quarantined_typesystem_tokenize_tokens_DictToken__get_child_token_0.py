
import pytest
from typesystem.tokenize.tokens import Token
from typesystem.tokenize.dict_token import DictToken

# Scenario 1: Test the initialization of a DictToken with tokenized values
@pytest.fixture(scope="module")
def tokenized_dict():
    return {
        "key1": Token("value1"),
        "key2": Token("value2")
    }

@pytest.mark.parametrize("key, expected", [("key1", "value1"), ("key2", "value2")])
def test_get_child_token(tokenized_dict, key, expected):
    dict_token = DictToken(value=tokenized_dict)
    assert dict_token._get_child_token(key)._value == expected

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
_ ERROR collecting test_typesystem_tokenize_tokens_DictToken__get_child_token_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokens_DictToken__get_child_token_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokens_DictToken__get_child_token_0.py:4: in <module>
    from typesystem.tokenize.dict_token import DictToken
E   ModuleNotFoundError: No module named 'typesystem.tokenize.dict_token'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokens_DictToken__get_child_token_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.21s ===============================
"""
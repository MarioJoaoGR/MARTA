
import pytest
from typesystem.tokenize import tokenize_yaml
from typesystem.exceptions import ParseError
from yaml import SafeLoader
import yaml
import typing

# Scenario 1: Test standard input with valid YAML content
def test_valid_yaml():
    yaml_content = "key: value"
    tokens = tokenize_yaml(yaml_content)
    assert isinstance(tokens, dict), f"Expected a dictionary but got {type(tokens)}"
    assert 'key' in tokens and tokens['key'] == 'value', f"Unexpected content: {tokens}"

# Scenario 2: Test empty input string
def test_empty_input():
    yaml_content = ""
    with pytest.raises(ParseError) as excinfo:
        tokenize_yaml(yaml_content)
    assert "No content." in str(excinfo.value), f"Expected 'no_content' error but got {str(excinfo.value)}"

# Scenario 3: Test input with invalid YAML syntax
def test_invalid_yaml():
    yaml_content = "key:"
    with pytest.raises(ParseError) as excinfo:
        tokenize_yaml(yaml_content)
    assert "Expected content of type 'block' or 'flow'" in str(excinfo.value), f"Unexpected error message: {str(excinfo.value)}"

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
__ ERROR collecting test_typesystem_tokenize_tokenize_yaml_tokenize_yaml_0.py __
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_yaml_tokenize_yaml_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_yaml_tokenize_yaml_0.py:4: in <module>
    from typesystem.exceptions import ParseError
E   ModuleNotFoundError: No module named 'typesystem.exceptions'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_yaml_tokenize_yaml_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.18s ===============================
"""
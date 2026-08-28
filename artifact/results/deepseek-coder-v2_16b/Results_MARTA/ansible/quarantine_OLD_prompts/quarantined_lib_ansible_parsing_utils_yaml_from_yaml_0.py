
import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.utils.yaml_loader import safe_load as _safe_load
from ansible.errors import AnsibleParserError
import yaml

# Define the function to be tested
def from_yaml(data, file_name='<string>', show_content=True, vault_secrets=None, json_only=False):
    '''
    Creates a Python datastructure from the given data, which can be either a JSON or YAML string. If the data is not valid JSON, it attempts to parse
    it as YAML and handles any errors that occur during parsing. The function supports optional parameters for specifying whether to display content on error, 
    provide vault secrets for decryption, and specify if only JSON should be parsed. It returns a Python dictionary or list representing the parsed data structure.

    Parameters:
        data (str or file-like object): The input data to be parsed. This can be a JSON or YAML formatted string or a file stream containing such data.
        file_name (str, optional): The name of the file from which the data is read. Defaults to '<string>'. If `data` is a string, this parameter is ignored.
        show_content (bool, optional): A flag indicating whether to include the content in the error message for display. Defaults to True. This option is relevant when parsing fails and an error needs to be displayed.
        vault_secrets (dict or None, optional): Any secrets that need to be handled by a vault plugin if the content requires decryption. If not provided, no decryption will occur. Defaults to None.
        json_only (bool, optional): A flag indicating whether only JSON should be attempted for parsing. If True and parsing fails, an exception is raised. Defaults to False.

    Returns:
        dict or list: The parsed Python datastructure from the input data. This will be a dictionary if the data is YAML, and a list (if applicable) after successful JSON parsing.

    Raises:
        AnsibleParserError: If `json_only` is True and parsing fails due to invalid JSON or malformed content, an exception is raised with details about the error.
    '''
    new_data = None

    try:
        # in case we have to deal with vaults
        _safe_load.set_secrets(vault_secrets)

        # we first try to load this data as JSON.
        # Fixes issues with extra vars json strings not being parsed correctly by the yaml parser
        new_data = yaml.safe_load(data)
    except Exception as json_exc:

        if json_only:
            raise AnsibleParserError(str(json_exc), orig_exc=json_exc)

        # must not be JSON, let the rest try
        try:
            new_data = _safe_load(data, file_name=file_name, vault_secrets=vault_secrets)
        except yaml.YAMLError as yaml_exc:
            raise AnsibleParserError(str(yaml_exc), orig_exc=yaml_exc)

    return new_data

# Test cases for the from_yaml function
def test_from_yaml_valid_json():
    data = '{"key": "value"}'
    result = from_yaml(data, json_only=True)
    assert isinstance(result, dict)
    assert result['key'] == 'value'

def test_from_yaml_invalid_json():
    data = 'invalid json'
    with pytest.raises(AnsibleParserError):
        from_yaml(data, json_only=True)

def test_from_yaml_valid_yaml():
    data = "key: value"
    result = from_yaml(data)
    assert isinstance(result, dict)
    assert result['key'] == 'value'

def test_from_yaml_invalid_yaml():
    data = "invalid yaml"
    with pytest.raises(AnsibleParserError):
        from_yaml(data)

@patch('ansible.parsing.utils.yaml_loader._safe_load', side_effect=Exception("Mocked YAML parsing error"))
def test_from_yaml_json_only_error(_mock_safe_load):
    data = '{"key": "value"}'
    with pytest.raises(AnsibleParserError) as excinfo:
        from_yaml(data, json_only=True)
    assert str(excinfo.value) == "Mocked YAML parsing error"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____ ERROR collecting test_lib_ansible_parsing_utils_yaml_from_yaml_0.py ______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_utils_yaml_from_yaml_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_utils_yaml_from_yaml_0.py:4: in <module>
    from ansible.parsing.utils.yaml_loader import safe_load as _safe_load
E   ModuleNotFoundError: No module named 'ansible.parsing.utils.yaml_loader'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_utils_yaml_from_yaml_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.23s ===============================
"""
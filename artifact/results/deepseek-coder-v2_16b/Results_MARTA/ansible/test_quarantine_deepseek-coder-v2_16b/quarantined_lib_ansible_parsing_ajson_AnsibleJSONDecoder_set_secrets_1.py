
import pytest
from ansible.parsing.ajson import AnsibleJSONDecoder
from ansible_vault import VaultLib
import json

def test_set_secrets():
    secrets = {'password': 'secret'}
    AnsibleJSONDecoder.set_secrets(secrets)
    assert isinstance(AnsibleJSONDecoder._vaults['default'], VaultLib)
    assert AnsibleJSONDecoder._vaults['default'].secrets == secrets

def test_init_with_object_hook():
    secrets = {'password': 'secret'}
    vaults = {'my_vault': VaultLib('password')}
    decoder = AnsibleJSONDecoder(object_hook=lambda obj: decode_obj(obj, vaults))
    assert isinstance(decoder._vaults['default'], VaultLib)
    assert decoder._vaults['default'].secrets == secrets

def test_json_loads_with_default_vault():
    secrets = {'password': 'secret'}
    AnsibleJSONDecoder.set_secrets(secrets)
    json_data = '{"key": "value"}'
    decoded_data = json.loads(json_data, cls=AnsibleJSONDecoder)
    assert decoded_data['key'] == 'value'

def test_json_loads_with_specific_vault():
    secrets = {'password': 'secret'}
    vaults = {'my_vault': VaultLib('password')}
    decoder = AnsibleJSONDecoder(object_hook=lambda obj: decode_obj(obj, vaults))
    json_data = '{"key": "value"}'
    decoded_data = json.loads(json_data, cls=decoder)
    assert decoded_data['key'] == 'value'

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
_ ERROR collecting test_lib_ansible_parsing_ajson_AnsibleJSONDecoder_set_secrets_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_ajson_AnsibleJSONDecoder_set_secrets_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_ajson_AnsibleJSONDecoder_set_secrets_1.py:4: in <module>
    from ansible_vault import VaultLib
E   ModuleNotFoundError: No module named 'ansible_vault'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_ajson_AnsibleJSONDecoder_set_secrets_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.73s ===============================
"""
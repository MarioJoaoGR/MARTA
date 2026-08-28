
import pytest
from ansible.plugins.filter.core import to_yaml
from ansible.module_utils.common.json import AnsibleDumper
from ansible.errors import AnsibleFilterError

def test_to_yaml_basic_conversion():
    data = {'key': 'value'}
    result = to_yaml(data)
    assert isinstance(result, str), "Expected a string output"
    assert result == yaml.dump(data), "Output does not match expected YAML format"

def test_to_yaml_custom_flow_style():
    data = {'key': 'value'}
    result = to_yaml(data, default_flow_style=True)
    assert isinstance(result, str), "Expected a string output"
    expected_output = yaml.dump(data, default_flow_style=True)
    assert result == expected_output, "Output does not match expected YAML format with custom flow style"

def test_to_yaml_error_handling():
    data = ['invalid', 'input']  # Invalid input to trigger an error
    with pytest.raises(AnsibleFilterError):
        to_yaml(data)

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
______ ERROR collecting test_lib_ansible_plugins_filter_core_to_yaml_0.py ______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_yaml_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_yaml_0.py:4: in <module>
    from ansible.module_utils.common.json import AnsibleDumper
E   ImportError: cannot import name 'AnsibleDumper' from 'ansible.module_utils.common.json' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/common/json.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_yaml_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.60s ===============================
"""
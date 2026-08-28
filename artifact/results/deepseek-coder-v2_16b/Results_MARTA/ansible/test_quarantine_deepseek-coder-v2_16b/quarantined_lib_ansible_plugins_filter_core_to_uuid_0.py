
import pytest
import uuid
from ansible.plugins.filter.core import to_uuid
from ansible.errors import AnsibleFilterError

# Define a fixed UUID namespace for testing
UUID_NAMESPACE_ANSIBLE = uuid.UUID('ansible-default-namespace')

def test_to_uuid_with_default_namespace():
    result = to_uuid('example')
    assert isinstance(result, uuid.UUID)
    assert str(result) == '6e3ab9a0-f4b7-5fee-81d2-9ffe7c6faa7e'

def test_to_uuid_with_custom_namespace():
    custom_namespace = uuid.UUID('12345678-1234-1234-1234-1234567890ab')
    result = to_uuid('example', custom_namespace)
    assert isinstance(result, uuid.UUID)
    assert str(result) == 'c9a8f8e3-b7d2-5fee-81d2-9ffe7c6faa7e'

def test_to_uuid_with_invalid_namespace():
    with pytest.raises(AnsibleFilterError):
        to_uuid('example', 'invalid-namespace')

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
______ ERROR collecting test_lib_ansible_plugins_filter_core_to_uuid_0.py ______
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_uuid_0.py:8: in <module>
    UUID_NAMESPACE_ANSIBLE = uuid.UUID('ansible-default-namespace')
/opt/conda/envs/test4py_env/lib/python3.10/uuid.py:177: in __init__
    raise ValueError('badly formed hexadecimal UUID string')
E   ValueError: badly formed hexadecimal UUID string
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_uuid_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.64s ===============================
"""
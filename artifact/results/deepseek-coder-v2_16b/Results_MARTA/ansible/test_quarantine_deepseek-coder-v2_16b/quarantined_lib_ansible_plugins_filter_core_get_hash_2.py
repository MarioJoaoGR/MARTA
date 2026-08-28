
import pytest
from ansible.plugins.filter.core import get_hash

def to_bytes(text, errors='surrogate_or_strict'):
    if isinstance(text, bytes):
        return text
    elif isinstance(text, str):
        return text.encode(errors=errors)
    else:
        raise TypeError("to_bytes must be called with a string type")

def get_hash(data, hashtype='sha1'):
    try:
        h = hashlib.new(hashtype)
    except Exception as e:
        # hash is not supported?
        raise AnsibleFilterError(e)

    h.update(to_bytes(data, errors='surrogate_or_strict'))
    return h.hexdigest()


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_get_hash_2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_valid_input_string ____________________________

data = 'hello world', hashtype = 'sha1'

    def get_hash(data, hashtype='sha1'):
        try:
>           h = hashlib.new(hashtype)
E           NameError: name 'hashlib' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_get_hash_2.py:15: NameError

During handling of the above exception, another exception occurred:

    def test_valid_input_string():
        data = 'hello world'
>       result = get_hash(data)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_get_hash_2.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

data = 'hello world', hashtype = 'sha1'

    def get_hash(data, hashtype='sha1'):
        try:
            h = hashlib.new(hashtype)
        except Exception as e:
            # hash is not supported?
>           raise AnsibleFilterError(e)
E           NameError: name 'AnsibleFilterError' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_get_hash_2.py:18: NameError
____________________________ test_valid_input_bytes ____________________________

data = b'hello world', hashtype = 'sha1'

    def get_hash(data, hashtype='sha1'):
        try:
>           h = hashlib.new(hashtype)
E           NameError: name 'hashlib' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_get_hash_2.py:15: NameError

During handling of the above exception, another exception occurred:

    def test_valid_input_bytes():
        data = b'hello world'
>       result = get_hash(data)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_get_hash_2.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

data = b'hello world', hashtype = 'sha1'

    def get_hash(data, hashtype='sha1'):
        try:
            h = hashlib.new(hashtype)
        except Exception as e:
            # hash is not supported?
>           raise AnsibleFilterError(e)
E           NameError: name 'AnsibleFilterError' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_get_hash_2.py:18: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_get_hash_2.py::test_valid_input_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_get_hash_2.py::test_valid_input_bytes
============================== 2 failed in 0.89s ===============================
"""

import pytest
from ansible.template.native_helpers import ansible_native_concat
from string import string_types

def test_ansible_native_concat_single_node():
    nodes = [1]
    result = ansible_native_concat(nodes)
    assert result == 1

def test_ansible_native_concat_multiple_nodes():
    nodes = ['a', 'b', 'c']
    result = ansible_native_concat(nodes)
    assert result == 'abc'

def test_ansible_native_concat_empty_list():
    nodes = []
    result = ansible_native_concat(nodes)
    assert result is None

def test_ansible_native_concat_generator():
    def generate_nodes():
        yield 'a'
        yield 'b'
        yield 'c'
    
    nodes = generate_nodes()
    result = ansible_native_concat(nodes)
    assert result == 'abc'

def test_ansible_native_concat_expression_in_node():
    nodes = ["'hello'", "'world'"]
    result = ansible_native_concat(nodes)
    assert result == "hello' 'world"

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
_ ERROR collecting test_lib_ansible_template_native_helpers_ansible_native_concat_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_native_helpers_ansible_native_concat_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_native_helpers_ansible_native_concat_0.py:4: in <module>
    from string import string_types
E   ImportError: cannot import name 'string_types' from 'string' (/opt/conda/envs/test4py_env/lib/python3.10/string.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_native_helpers_ansible_native_concat_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.63s ===============================
"""
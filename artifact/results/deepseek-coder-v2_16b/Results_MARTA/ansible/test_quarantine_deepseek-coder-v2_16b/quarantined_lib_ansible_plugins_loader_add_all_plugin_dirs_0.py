
import os
from unittest.mock import patch
import pytest
from ansible.plugins.loader import PluginPathContext, get_all_plugin_loaders
from ansible.utils import to_bytes, to_text
from ansible.playbook.display_common import display

def add_all_plugin_dirs(path):
    ''' Add any existing plugin dirs in the path provided, expanding user home directory if necessary. It checks each potential plugin subdirectory for validity and adds it as a plugin directory if found. If the provided path is not a directory, it warns about the invalid path. '''
    b_path = os.path.expanduser(to_bytes(path, errors='surrogate_or_strict'))
    if os.path.isdir(b_path):
        for name, obj in get_all_plugin_loaders():
            if obj.subdir:
                plugin_path = os.path.join(b_path, to_bytes(obj.subdir))
                if os.path.isdir(plugin_path):
                    obj.add_directory(to_text(plugin_path))
    else:
        display.warning("Ignoring invalid path provided to plugin path: '%s' is not a directory" % to_text(path))

def test_invalid_input_error_handling():
    with patch('os.path.isdir', return_value=False):
        with pytest.warns(UserWarning) as record:
            add_all_plugin_dirs('invalid-path')
        assert len(record) == 1, "Expected one warning but got none"
        assert str(record[0].message) == "Ignoring invalid path provided to plugin path: 'invalid-path' is not a directory"

def test_edge_case_none_input():
    with pytest.raises(TypeError):
        add_all_plugin_dirs(None)

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
__ ERROR collecting test_lib_ansible_plugins_loader_add_all_plugin_dirs_0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_loader_add_all_plugin_dirs_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_loader_add_all_plugin_dirs_0.py:6: in <module>
    from ansible.utils import to_bytes, to_text
E   ImportError: cannot import name 'to_bytes' from 'ansible.utils' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_loader_add_all_plugin_dirs_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.61s ===============================
"""
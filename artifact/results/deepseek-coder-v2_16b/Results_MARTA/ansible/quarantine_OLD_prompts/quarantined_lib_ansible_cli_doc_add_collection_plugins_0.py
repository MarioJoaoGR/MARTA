
import pytest
from unittest.mock import patch
from ansible.cli.doc import DocCLI
import os
from ansible.utils.path import to_text
from ansible.module_utils._text import _get_collection_name_from_path
from ansible.plugins.loader import list_collection_dirs, C

def add_collection_plugins(plugin_list, plugin_type, coll_filter=None):
    """
    Adds plugins to a list from specified collection directories based on the given plugin type and optional collection filter.

    Parameters:
        plugin_list (list): A list where found plugins will be added. This parameter is required and should be a mutable sequence that supports item assignment, such as a Python list.
        plugin_type (str): The type of plugin to search for, e.g., 'module', 'docuri'. This parameter is required and specifies the kind of plugin you are looking for in the collection directories.
        coll_filter (str, optional): A filter string to specify which collections' directories should be searched. If provided, only directories matching this filter will be considered when searching for plugins. Defaults to None, meaning all collection directories will be searched.

    Returns:
        None: The function modifies the input `plugin_list` in place by adding found plugins to it.

    Examples:
        Adding modules from a specific type of collections:
        ```python
        plugin_list = []
        add_collection_plugins(plugin_list, 'module', coll_filter='specific_type')
        ```
        This example will search within collection directories that match the filter 'specific_type' and add found module plugins to `plugin_list`.

    Notes:
        The function assumes that the paths provided in `coll_filter` are correct and accessible. It also handles cases where no matching collection directories or plugins are found, doing nothing in such scenarios.
    """
    b_colldirs = list_collection_dirs(coll_filter=coll_filter)
    for b_path in b_colldirs:
        path = to_text(b_path, errors='surrogate_or_strict')
        collname = _get_collection_name_from_path(b_path)
        ptype = C.COLLECTION_PTYPE_COMPAT.get(plugin_type, plugin_type)
        plugin_list.update(DocCLI.find_plugins(os.path.join(path, 'plugins', ptype), False, plugin_type, collection=collname))

# Test cases for add_collection_plugins function
def test_valid_inputs():
    with patch('ansible.cli.doc.DocCLI.find_plugins', return_value=['plugin1', 'plugin2']):
        plugin_list = []
        add_collection_plugins(plugin_list, 'module')
        assert len(plugin_list) == 2
        assert 'plugin1' in plugin_list
        assert 'plugin2' in plugin_list

def test_edge_cases():
    with patch('ansible.cli.doc.DocCLI.find_plugins', return_value=[]):
        plugin_list = []
        add_collection_plugins(plugin_list, 'module')
        assert len(plugin_list) == 0

def test_invalid_inputs():
    with pytest.raises(TypeError):
        plugin_list = []
        add_collection_plugins(plugin_list, 'module', coll_filter='specific_type')
        add_collection_plugins(plugin_list, 123)

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
____ ERROR collecting test_lib_ansible_cli_doc_add_collection_plugins_0.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_add_collection_plugins_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_add_collection_plugins_0.py:7: in <module>
    from ansible.module_utils._text import _get_collection_name_from_path
E   ImportError: cannot import name '_get_collection_name_from_path' from 'ansible.module_utils._text' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/_text.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_add_collection_plugins_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.69s ===============================
"""
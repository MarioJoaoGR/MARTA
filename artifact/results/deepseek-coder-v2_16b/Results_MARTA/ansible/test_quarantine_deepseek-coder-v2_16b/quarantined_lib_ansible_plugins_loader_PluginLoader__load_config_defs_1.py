
import pytest
from ansible.plugins.loader import PluginLoader

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_loader_PluginLoader__load_config_defs_1.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        loader = PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')
>       plugin = loader.get('example_plugin')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_loader_PluginLoader__load_config_defs_1.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/loader.py:807: in get
    return self.get_with_context(name, *args, **kwargs).object
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/loader.py:817: in get_with_context
    plugin_load_context = self.find_plugin_with_context(name, collection_list=collection_list)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/loader.py:559: in find_plugin_with_context
    result = self._resolve_plugin_step(name, mod_type, ignore_deprecated, check_aliases, collection_list, plugin_load_context=plugin_load_context)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/loader.py:655: in _resolve_plugin_step
    return self._find_plugin_legacy(name, plugin_load_context, ignore_deprecated, check_aliases, suffix)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/loader.py:685: in _find_plugin_legacy
    for path_with_context in (p for p in self._get_paths_with_context() if p.path not in self._searched_paths and os.path.isdir(to_bytes(p.path))):
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/loader.py:345: in _get_paths_with_context
    path = os.path.abspath(os.path.expanduser(path))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = {'plugin1': '/path/to/config1'}

    def expanduser(path):
        """Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing."""
>       path = os.fspath(path)
E       TypeError: expected str, bytes or os.PathLike object, not dict

/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py:232: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_loader_PluginLoader__load_config_defs_1.py::test_valid_case
============================== 1 failed in 0.86s ===============================
"""
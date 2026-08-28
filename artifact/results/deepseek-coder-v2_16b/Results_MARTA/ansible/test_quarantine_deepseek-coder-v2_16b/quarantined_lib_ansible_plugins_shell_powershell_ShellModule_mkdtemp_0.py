
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_mkdtemp_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f76ec6a4040>

    def test_valid_inputs(shell_module):
>       temp_script = shell_module.mkdtemp(basefile='test_dir')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_mkdtemp_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/shell/powershell.py:126: in mkdtemp
    basetmpdir = tmpdir if tmpdir else self.get_option('remote_tmp')
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.shell.powershell.ShellModule object at 0x7f76ec6a4040>
option = 'remote_tmp', hostvars = None

    def get_option(self, option, hostvars=None):
        if option not in self._options:
            try:
>               option_value = C.config.get_config_value(option, plugin_type=get_plugin_class(self), plugin_name=self._load_name, variables=hostvars)
E               AttributeError: 'ShellModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:58: AttributeError
_______________________________ test_edge_cases ________________________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f76ec6a4040>

    def test_edge_cases(shell_module):
>       temp_script = shell_module.mkdtemp(basefile=None)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_mkdtemp_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/shell/powershell.py:126: in mkdtemp
    basetmpdir = tmpdir if tmpdir else self.get_option('remote_tmp')
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.shell.powershell.ShellModule object at 0x7f76ec6a4040>
option = 'remote_tmp', hostvars = None

    def get_option(self, option, hostvars=None):
        if option not in self._options:
            try:
>               option_value = C.config.get_config_value(option, plugin_type=get_plugin_class(self), plugin_name=self._load_name, variables=hostvars)
E               AttributeError: 'ShellModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:58: AttributeError
_____________________________ test_invalid_inputs ______________________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f76ec6a4040>

    def test_invalid_inputs(shell_module):
        with pytest.raises(TypeError):
>           shell_module.mkdtemp(basefile=123)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_mkdtemp_0.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/shell/powershell.py:126: in mkdtemp
    basetmpdir = tmpdir if tmpdir else self.get_option('remote_tmp')
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.shell.powershell.ShellModule object at 0x7f76ec6a4040>
option = 'remote_tmp', hostvars = None

    def get_option(self, option, hostvars=None):
        if option not in self._options:
            try:
>               option_value = C.config.get_config_value(option, plugin_type=get_plugin_class(self), plugin_name=self._load_name, variables=hostvars)
E               AttributeError: 'ShellModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:58: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_mkdtemp_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_mkdtemp_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_mkdtemp_0.py::test_invalid_inputs
============================== 3 failed in 0.46s ===============================
"""
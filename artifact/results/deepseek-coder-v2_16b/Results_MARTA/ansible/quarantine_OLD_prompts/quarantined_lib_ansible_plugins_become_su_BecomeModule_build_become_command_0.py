
import pytest
from unittest.mock import patch
from ansible.plugins.become.su import BecomeModule


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_become_su_BecomeModule_build_become_command_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        su_module = BecomeModule()
        with patch('ansible.plugins.become.su.shlex_quote', return_value="'ls -l'"):
>           result = su_module.build_become_command('ls -l', True)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_become_su_BecomeModule_build_become_command_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/become/su.py:156: in build_become_command
    exe = self.get_option('become_exe') or self.name
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/become/__init__.py:48: in get_option
    return super(BecomeBase, self).get_option(option, hostvars=hostvars)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.become.su.BecomeModule object at 0x7f3f9eececb0>
option = 'become_exe', hostvars = None

    def get_option(self, option, hostvars=None):
        if option not in self._options:
            try:
>               option_value = C.config.get_config_value(option, plugin_type=get_plugin_class(self), plugin_name=self._load_name, variables=hostvars)
E               AttributeError: 'BecomeModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:58: AttributeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        su_module = BecomeModule()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_become_su_BecomeModule_build_become_command_0.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_become_su_BecomeModule_build_become_command_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_become_su_BecomeModule_build_become_command_0.py::test_invalid_input
============================== 2 failed in 0.40s ===============================
"""
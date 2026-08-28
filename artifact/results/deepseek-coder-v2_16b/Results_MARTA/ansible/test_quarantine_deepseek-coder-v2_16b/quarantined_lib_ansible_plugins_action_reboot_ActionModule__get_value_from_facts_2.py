
import pytest
from ansible.plugins.action import reboot


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_action_reboot_ActionModule__get_value_from_facts_2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
>       instance = reboot.ActionModule(connection='local', module_name='reboot', tmpdir=None)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_action_reboot_ActionModule__get_value_from_facts_2.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.action.reboot.ActionModule object at 0x7f531d7b61d0>
args = ()
kwargs = {'connection': 'local', 'module_name': 'reboot', 'tmpdir': None}

    def __init__(self, *args, **kwargs):
>       super(ActionModule, self).__init__(*args, **kwargs)
E       TypeError: ActionBase.__init__() got an unexpected keyword argument 'module_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/action/reboot.py:87: TypeError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
>       instance = reboot.ActionModule(connection='local', module_name='reboot', tmpdir=None)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_action_reboot_ActionModule__get_value_from_facts_2.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.action.reboot.ActionModule object at 0x7f531d6cb910>
args = ()
kwargs = {'connection': 'local', 'module_name': 'reboot', 'tmpdir': None}

    def __init__(self, *args, **kwargs):
>       super(ActionModule, self).__init__(*args, **kwargs)
E       TypeError: ActionBase.__init__() got an unexpected keyword argument 'module_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/action/reboot.py:87: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_action_reboot_ActionModule__get_value_from_facts_2.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_action_reboot_ActionModule__get_value_from_facts_2.py::test_edge_cases
============================== 2 failed in 0.98s ===============================
"""
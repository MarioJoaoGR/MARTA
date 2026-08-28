
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.iptables import push_arguments

def set_chain_policy(iptables_path, module, params):
    cmd = push_arguments(iptables_path, '-P', params['table'], params['chain'], make_rule=False)
    cmd.append(params['policy'])
    module.run_command(cmd, check_rc=True)

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.run_command = MagicMock()
    return module

@pytest.mark.parametrize("params", [
    ({'table': 'filter', 'chain': 'INPUT', 'policy': 'DROP'}),
    ({'table': 'nat', 'chain': 'OUTPUT', 'policy': 'ACCEPT'}),
    ({'table': 'filter', 'chain': 'FORWARD', 'policy': 'QUEUE'})
])
def test_set_chain_policy(params, mock_module):
    with patch('ansible.modules.iptables.push_arguments', return_value=['/usr/sbin/iptables', '-P', params['table'], params['chain'], 'DROP'] if params['policy'] == 'DROP' else ['/usr/sbin/iptables', '-P', params['table'], params['chain'], 'QUEUE']):
        set_chain_policy('/usr/sbin/iptables', mock_module, params)
        expected_cmd = ['/usr/sbin/iptables', '-P', params['table'], params['chain'], params['policy']]
        mock_module.run_command.assert_called_with(expected_cmd, check_rc=True)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_set_chain_policy_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_set_chain_policy[params0] ________________________

params = {'chain': 'INPUT', 'policy': 'DROP', 'table': 'filter'}
mock_module = <MagicMock id='140415073287424'>

    @pytest.mark.parametrize("params", [
        ({'table': 'filter', 'chain': 'INPUT', 'policy': 'DROP'}),
        ({'table': 'nat', 'chain': 'OUTPUT', 'policy': 'ACCEPT'}),
        ({'table': 'filter', 'chain': 'FORWARD', 'policy': 'QUEUE'})
    ])
    def test_set_chain_policy(params, mock_module):
        with patch('ansible.modules.iptables.push_arguments', return_value=['/usr/sbin/iptables', '-P', params['table'], params['chain'], 'DROP'] if params['policy'] == 'DROP' else ['/usr/sbin/iptables', '-P', params['table'], params['chain'], 'QUEUE']):
>           set_chain_policy('/usr/sbin/iptables', mock_module, params)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_set_chain_policy_0.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

iptables_path = '/usr/sbin/iptables', module = <MagicMock id='140415073287424'>
params = {'chain': 'INPUT', 'policy': 'DROP', 'table': 'filter'}

    def set_chain_policy(iptables_path, module, params):
>       cmd = push_arguments(iptables_path, '-P', params['table'], params['chain'], make_rule=False)
E       TypeError: push_arguments() got multiple values for argument 'make_rule'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_set_chain_policy_0.py:7: TypeError
________________________ test_set_chain_policy[params1] ________________________

params = {'chain': 'OUTPUT', 'policy': 'ACCEPT', 'table': 'nat'}
mock_module = <MagicMock id='140415073287664'>

    @pytest.mark.parametrize("params", [
        ({'table': 'filter', 'chain': 'INPUT', 'policy': 'DROP'}),
        ({'table': 'nat', 'chain': 'OUTPUT', 'policy': 'ACCEPT'}),
        ({'table': 'filter', 'chain': 'FORWARD', 'policy': 'QUEUE'})
    ])
    def test_set_chain_policy(params, mock_module):
        with patch('ansible.modules.iptables.push_arguments', return_value=['/usr/sbin/iptables', '-P', params['table'], params['chain'], 'DROP'] if params['policy'] == 'DROP' else ['/usr/sbin/iptables', '-P', params['table'], params['chain'], 'QUEUE']):
>           set_chain_policy('/usr/sbin/iptables', mock_module, params)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_set_chain_policy_0.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

iptables_path = '/usr/sbin/iptables', module = <MagicMock id='140415073287664'>
params = {'chain': 'OUTPUT', 'policy': 'ACCEPT', 'table': 'nat'}

    def set_chain_policy(iptables_path, module, params):
>       cmd = push_arguments(iptables_path, '-P', params['table'], params['chain'], make_rule=False)
E       TypeError: push_arguments() got multiple values for argument 'make_rule'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_set_chain_policy_0.py:7: TypeError
________________________ test_set_chain_policy[params2] ________________________

params = {'chain': 'FORWARD', 'policy': 'QUEUE', 'table': 'filter'}
mock_module = <MagicMock id='140415075189952'>

    @pytest.mark.parametrize("params", [
        ({'table': 'filter', 'chain': 'INPUT', 'policy': 'DROP'}),
        ({'table': 'nat', 'chain': 'OUTPUT', 'policy': 'ACCEPT'}),
        ({'table': 'filter', 'chain': 'FORWARD', 'policy': 'QUEUE'})
    ])
    def test_set_chain_policy(params, mock_module):
        with patch('ansible.modules.iptables.push_arguments', return_value=['/usr/sbin/iptables', '-P', params['table'], params['chain'], 'DROP'] if params['policy'] == 'DROP' else ['/usr/sbin/iptables', '-P', params['table'], params['chain'], 'QUEUE']):
>           set_chain_policy('/usr/sbin/iptables', mock_module, params)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_set_chain_policy_0.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

iptables_path = '/usr/sbin/iptables', module = <MagicMock id='140415075189952'>
params = {'chain': 'FORWARD', 'policy': 'QUEUE', 'table': 'filter'}

    def set_chain_policy(iptables_path, module, params):
>       cmd = push_arguments(iptables_path, '-P', params['table'], params['chain'], make_rule=False)
E       TypeError: push_arguments() got multiple values for argument 'make_rule'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_set_chain_policy_0.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_set_chain_policy_0.py::test_set_chain_policy[params0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_set_chain_policy_0.py::test_set_chain_policy[params1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_set_chain_policy_0.py::test_set_chain_policy[params2]
============================== 3 failed in 0.29s ===============================
"""

import pytest
from ansible.vars.hostvars import HostVarsVars
import yaml

# Load variables for testing
with open('variables.yaml') as file:
    vars = yaml.safe_load(file)

@pytest.fixture(scope="module")
def host_vars():
    loader = MockLoader()  # Assuming a mock loader is needed, replace with actual implementation if necessary
    return HostVarsVars(vars, loader)

class MockLoader:
    def __init__(self):
        self.basedir = './'
    
    def get_basedir(self):
        return self.basedir

def test_get_variable(host_vars):
    variable = host_vars['host1']
    assert variable == {'var1': 'value1'}

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
__ ERROR collecting test_lib_ansible_vars_hostvars_HostVarsVars___init___1.py __
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_hostvars_HostVarsVars___init___1.py:7: in <module>
    with open('variables.yaml') as file:
E   FileNotFoundError: [Errno 2] No such file or directory: 'variables.yaml'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_hostvars_HostVarsVars___init___1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 1.03s ===============================
"""
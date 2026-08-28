
import pytest
from ansible.galaxy.api import GalaxyAPI
from ansible.errors import AnsibleError


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__add_auth_token_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_missing_token ______________________________

    def test_missing_token():
>       with pytest.raises(AnsibleError) as excinfo:
E       Failed: DID NOT RAISE <class 'ansible.errors.AnsibleError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__add_auth_token_0.py:7: Failed
_________________________ test_missing_token_required __________________________

    def test_missing_token_required():
        with pytest.raises(AnsibleError) as excinfo:
>           api_client = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com', required=True)
E           TypeError: GalaxyAPI.__init__() got an unexpected keyword argument 'required'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__add_auth_token_0.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__add_auth_token_0.py::test_missing_token
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__add_auth_token_0.py::test_missing_token_required
============================== 2 failed in 0.45s ===============================
"""
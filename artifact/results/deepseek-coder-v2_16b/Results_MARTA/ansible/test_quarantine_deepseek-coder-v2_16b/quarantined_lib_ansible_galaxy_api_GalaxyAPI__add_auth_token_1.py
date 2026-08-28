
import pytest
from ansible.galaxy.api import GalaxyAPI


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__add_auth_token_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_missing_token ______________________________

    def test_missing_token():
        with pytest.raises(Exception) as e:
            api = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com', required=True)
>       assert str(e.value) == "No access token or username set. A token can be set with --api-key or at /path/to/token."
E       assert "GalaxyAPI.__...nt 'required'" == 'No access to...ath/to/token.'
E         
E         - No access token or username set. A token can be set with --api-key or at /path/to/token.
E         + GalaxyAPI.__init__() got an unexpected keyword argument 'required'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__add_auth_token_1.py:8: AssertionError
____________________________ test_missing_username _____________________________

    def test_missing_username():
>       with pytest.raises(Exception) as e:
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__add_auth_token_1.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__add_auth_token_1.py::test_missing_token
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__add_auth_token_1.py::test_missing_username
============================== 2 failed in 0.82s ===============================
"""

import pytest
from ansible.galaxy.token import KeycloakToken


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_token_KeycloakToken__form_payload_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        keycloak_token = KeycloakToken(access_token=None, auth_url='', validate_certs=False, client_id='')
        assert keycloak_token.access_token is None
        assert keycloak_token.auth_url == ''
        assert keycloak_token.validate_certs is False
>       assert keycloak_token.client_id == 'cloud-services'
E       AssertionError: assert '' == 'cloud-services'
E         
E         - cloud-services

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_token_KeycloakToken__form_payload_0.py:10: AssertionError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_token_KeycloakToken__form_payload_0.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_token_KeycloakToken__form_payload_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_token_KeycloakToken__form_payload_0.py::test_invalid_inputs
============================== 2 failed in 0.44s ===============================
"""
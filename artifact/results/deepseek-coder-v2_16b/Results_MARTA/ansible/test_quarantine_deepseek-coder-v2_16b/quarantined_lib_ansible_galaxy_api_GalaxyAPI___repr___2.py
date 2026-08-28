
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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI___repr___2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_disable_cache ______________________________

    def test_disable_cache():
        api_client = GalaxyAPI(
            galaxy='another_galaxy',
            name='name_for_auth',
            url='https://another-server.com',
            no_cache=True,
            clear_response_cache=True
        )
>       assert hasattr(api_client, 'no_cache'), "Expected 'no_cache' attribute to be set"
E       AssertionError: Expected 'no_cache' attribute to be set
E       assert False
E        +  where False = hasattr(<name_for_auth "name_for_auth" @ https://another-server.com with priority inf>, 'no_cache')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI___repr___2.py:13: AssertionError
__________________________________ test_repr ___________________________________

    def test_repr():
        api_client = GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')
        expected_repr = "<{instance!s} '{name!s}' @ {url!s} with priority {priority!s}>".format(
            instance=api_client, name='default_name', url='https://api.ansiblegalaxy.com', priority=float('inf')
        )
>       assert repr(api_client) == expected_repr, "Expected the repr to match the format string"
E       AssertionError: Expected the repr to match the format string
E       assert '<default_nam...priority inf>' == '<default_nam...priority inf>'
E         
E         Skipping 42 identical trailing characters in diff, use -v to show
E         - <default_name 'default_name' @ https:
E         ?               ^            ^
E         + <default_name "default_name" @ https:
E         ?               ^            ^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI___repr___2.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI___repr___2.py::test_disable_cache
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI___repr___2.py::test_repr
============================== 2 failed in 0.80s ===============================
"""
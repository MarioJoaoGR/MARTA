
import pytest
from ansible.plugins.lookup.ini import _parse_params



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_ini__parse_params_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        term = 'key1=value1 key2=value2'
        paramvals = {'key1': '', 'key2': ''}
        result = _parse_params(term, paramvals)
>       assert result == ['value1', 'value2']
E       AssertionError: assert ['key1=value1', 'key2=value2'] == ['value1', 'value2']
E         
E         At index 0 diff: 'key1=value1' != 'value1'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_ini__parse_params_0.py:9: AssertionError
_______________________________ test_none_input ________________________________

    def test_none_input():
        term = None
        paramvals = {'key1': '', 'key2': ''}
        with pytest.raises(TypeError):
>           _parse_params(term, paramvals)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_ini__parse_params_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

term = None, paramvals = {'key1': '', 'key2': ''}

    def _parse_params(term, paramvals):
        '''Safely split parameter term to preserve spaces'''
    
        # TODO: deprecate this method
        valid_keys = paramvals.keys()
        params = defaultdict(lambda: '')
    
        # TODO: check kv_parser to see if it can handle spaces this same way
        keys = []
        thiskey = 'key'  # initialize for 'lookup item'
>       for idp, phrase in enumerate(term.split()):
E       AttributeError: 'NoneType' object has no attribute 'split'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/ini.py:102: AttributeError
____________________________ test_invalid_paramvals ____________________________

    def test_invalid_paramvals():
        term = 'key1=value1 key2=value2'
        paramvals = {}
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_ini__parse_params_0.py:20: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_ini__parse_params_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_ini__parse_params_0.py::test_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_ini__parse_params_0.py::test_invalid_paramvals
============================== 3 failed in 0.39s ===============================
"""
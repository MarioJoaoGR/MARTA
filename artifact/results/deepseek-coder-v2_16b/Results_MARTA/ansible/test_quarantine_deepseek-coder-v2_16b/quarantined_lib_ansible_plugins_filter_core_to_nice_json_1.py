
import pytest
from ansible.plugins.filter import core



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_nice_json_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________________ test_to_nice_json_with_default_settings ____________________

    def test_to_nice_json_with_default_settings():
        data = {'key': 'value'}
        result = core.to_nice_json(data)
        assert isinstance(result, str), "Expected a string representation"
        assert '"key": "value"' in result, "Expected the key-value pair to be present"
>       assert result == '{\n  "key": "value"\n}', "Expected formatted JSON with indentation and sorted keys"
E       AssertionError: Expected formatted JSON with indentation and sorted keys
E       assert '{\n    "key": "value"\n}' == '{\n  "key": "value"\n}'
E         
E           {
E         -   "key": "value"
E         +     "key": "value"
E         ? ++
E           }

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_nice_json_1.py:10: AssertionError
____________________ test_to_nice_json_with_disable_sorting ____________________

    def test_to_nice_json_with_disable_sorting():
        data = {'key': 'value'}
        result = core.to_nice_json(data, sort_keys=False)
        assert isinstance(result, str), "Expected a string representation"
        assert '"key": "value"' in result, "Expected the key-value pair to be present"
>       assert result == '{\n  "key": "value"\n}', "Expected formatted JSON with default indentation and unsorted keys"
E       AssertionError: Expected formatted JSON with default indentation and unsorted keys
E       assert '{\n    "key": "value"\n}' == '{\n  "key": "value"\n}'
E         
E           {
E         -   "key": "value"
E         +     "key": "value"
E         ? ++
E           }

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_nice_json_1.py:17: AssertionError
____________________ test_to_nice_json_with_additional_args ____________________

    def test_to_nice_json_with_additional_args():
        data = {'key': 'value'}
>       result = core.to_nice_json(data, indent=4, sort_keys=True, separators=(',', ': '))

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_nice_json_1.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

a = {'key': 'value'}, indent = 4, sort_keys = True, args = ()
kw = {'separators': (',', ': ')}

    def to_nice_json(a, indent=4, sort_keys=True, *args, **kw):
        '''Make verbose, human readable JSON'''
>       return to_json(a, indent=indent, sort_keys=sort_keys, separators=(',', ': '), *args, **kw)
E       TypeError: ansible.plugins.filter.core.to_json() got multiple values for keyword argument 'separators'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/filter/core.py:73: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_nice_json_1.py::test_to_nice_json_with_default_settings
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_nice_json_1.py::test_to_nice_json_with_disable_sorting
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_nice_json_1.py::test_to_nice_json_with_additional_args
============================== 3 failed in 0.82s ===============================
"""
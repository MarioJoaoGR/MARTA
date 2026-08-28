
import pytest
from ansible.module_utils.common.dict_transformations import camel_dict_to_snake_dict

def _camel_to_snake(name, reversible=False):
    if not reversible:
        # Regular conversion from camel to snake case
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    else:
        # Reversible conversion from snake to camel case and back
        if '_' in name:
            parts = name.split('_')
            return parts[0] + ''.join(part.capitalize() for part in parts[1:])
        else:
            return name




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camel_dict_to_snake_dict_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________ test_camel_dict_to_snake_dict_with_reversible _________________

    def test_camel_dict_to_snake_dict_with_reversible():
        camel_dict = {'HTTPEndpoint': {'nestedKey': ['listItem1', 'listItem2']}}
        expected_output = {'http_endpoint': {'nested_key': ['list_item1', 'list_item2']}}
>       assert camel_dict_to_snake_dict(camel_dict, reversible=True) == expected_output
E       AssertionError: assert {'h_t_t_p_end...'listItem2']}} == {'http_endpoi...list_item2']}}
E         
E         Left contains 1 more item:
E         {'h_t_t_p_endpoint': {'nested_key': ['listItem1', 'listItem2']}}
E         Right contains 1 more item:
E         {'http_endpoint': {'nested_key': ['list_item1', 'list_item2']}}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camel_dict_to_snake_dict_0.py:21: AssertionError
________________ test_camel_dict_to_snake_dict_with_ignore_list ________________

    def test_camel_dict_to_snake_dict_with_ignore_list():
        camel_dict = {'camelCaseKey': 'value', 'Tags': {'tagName': 'tagValue'}}
        expected_output = {'camel_case_key': 'value', 'Tags': {'tagName': 'tagValue'}}
>       assert camel_dict_to_snake_dict(camel_dict, ignore_list=('Tags',)) == expected_output
E       AssertionError: assert {'camel_case_...: 'tagValue'}} == {'Tags': {'ta...key': 'value'}
E         
E         Omitting 1 identical items, use -vv to show
E         Left contains 1 more item:
E         {'tags': {'tagName': 'tagValue'}}
E         Right contains 1 more item:
E         {'Tags': {'tagName': 'tagValue'}}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camel_dict_to_snake_dict_0.py:26: AssertionError
___________________ test_camel_dict_to_snake_dict_reversible ___________________

    def test_camel_dict_to_snake_dict_reversible():
        camel_dict = {'HTTPEndpoint': {'nestedKey': ['listItem1', 'listItem2']}}
        converted_dict = camel_dict_to_snake_dict(camel_dict, reversible=True)
>       assert camel_dict_to_snake_dict(converted_dict, reversible=True) == camel_dict
E       AssertionError: assert {'h_t_t_p_end...'listItem2']}} == {'HTTPEndpoin...'listItem2']}}
E         
E         Left contains 1 more item:
E         {'h_t_t_p_endpoint': {'nested_key': ['listItem1', 'listItem2']}}
E         Right contains 1 more item:
E         {'HTTPEndpoint': {'nestedKey': ['listItem1', 'listItem2']}}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camel_dict_to_snake_dict_0.py:31: AssertionError
_____________________ test_camel_dict_to_snake_dict_ignore _____________________

    def test_camel_dict_to_snake_dict_ignore():
        camel_dict = {'camelCaseKey': 'value', 'Tags': {'tagName': 'tagValue'}}
        expected_output = {'camel_case_key': 'value', 'Tags': {'tagName': 'tagValue'}}
>       assert camel_dict_to_snake_dict(camel_dict, ignore_list=('Tags',)) == expected_output
E       AssertionError: assert {'camel_case_...: 'tagValue'}} == {'Tags': {'ta...key': 'value'}
E         
E         Omitting 1 identical items, use -vv to show
E         Left contains 1 more item:
E         {'tags': {'tagName': 'tagValue'}}
E         Right contains 1 more item:
E         {'Tags': {'tagName': 'tagValue'}}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camel_dict_to_snake_dict_0.py:36: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camel_dict_to_snake_dict_0.py::test_camel_dict_to_snake_dict_with_reversible
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camel_dict_to_snake_dict_0.py::test_camel_dict_to_snake_dict_with_ignore_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camel_dict_to_snake_dict_0.py::test_camel_dict_to_snake_dict_reversible
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camel_dict_to_snake_dict_0.py::test_camel_dict_to_snake_dict_ignore
============================== 4 failed in 0.31s ===============================
"""

import pytest
from ansible.utils.unsafe_proxy import _wrap_dict, wrap_var





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_wrap_dict ________________________________

    def test_wrap_dict():
        # Basic usage
        result = _wrap_dict({'a': 1, 'b': [2, 'c']})
>       assert result == {'a': '"1"', 'b': ['"2"', '"c"']}
E       assert {'a': 1, 'b': [2, 'c']} == {'a': '"1"', ...'"2"', '"c"']}
E         
E         Differing items:
E         {'b': [2, 'c']} != {'b': ['"2"', '"c"']}
E         {'a': 1} != {'a': '"1"'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py:8: AssertionError
_____________________________ test_wrap_var_string _____________________________

    def test_wrap_var_string():
        # String type
>       assert wrap_var("hello") == '"hello"'
E       assert 'hello' == '"hello"'
E         
E         - "hello"
E         ? -     -
E         + hello

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py:12: AssertionError
____________________________ test_wrap_var_integer _____________________________

    def test_wrap_var_integer():
        # Integer type
>       assert wrap_var(1) == '"1"'
E       assert 1 == '"1"'
E        +  where 1 = wrap_var(1)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py:16: AssertionError
______________________________ test_wrap_var_list ______________________________

    def test_wrap_var_list():
        # List type
>       assert wrap_var([2, 'c']) == ['"2"', '"c"']
E       assert [2, 'c'] == ['"2"', '"c"']
E         
E         At index 0 diff: 2 != '"2"'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py:20: AssertionError
____________________________ test_wrap_dict_nested _____________________________

    def test_wrap_dict_nested():
        # Nested structure
        result = _wrap_dict({1: {2: "three", 3: ["four", "five"]}})
        expected = {'1': {'2': '"three"', '3': ['"four"', '"five"']}}
>       assert result == expected
E       assert {1: {2: 'thre...ur', 'five']}} == {'1': {'2': '...', '"five"']}}
E         
E         Left contains 1 more item:
E         {1: {2: 'three', 3: ['four', 'five']}}
E         Right contains 1 more item:
E         {'1': {'2': '"three"', '3': ['"four"', '"five"']}}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py:26: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py::test_wrap_dict
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py::test_wrap_var_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py::test_wrap_var_integer
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py::test_wrap_var_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy__wrap_dict_1.py::test_wrap_dict_nested
============================== 5 failed in 0.75s ===============================
"""
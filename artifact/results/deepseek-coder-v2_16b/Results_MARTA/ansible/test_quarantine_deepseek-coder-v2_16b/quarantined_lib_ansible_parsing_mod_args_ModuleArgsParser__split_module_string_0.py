
import pytest
from ansible.parsing.mod_args import ModuleArgsParser




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__split_module_string_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        task_ds = {'action': 'copy src=a dest=b'}
        collection_list = ['ansible.builtin']
        parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
        action, args, delegate_to = parser.parse()
    
        assert action == 'copy'
        assert args == {'src': 'a', 'dest': 'b'}
>       assert delegate_to is None
E       AssertionError: assert <class 'ansible.utils.sentinel.Sentinel'> is None

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__split_module_string_0.py:13: AssertionError
______________________________ test_local_action _______________________________

    def test_local_action():
        task_ds = {'local_action': 'shell echo hi'}
        collection_list = ['ansible.builtin']
        parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
        action, args, delegate_to = parser.parse()
    
        assert action == 'shell'
>       assert args == {'echo': 'hi'}
E       AssertionError: assert {'_raw_params': 'echo hi'} == {'echo': 'hi'}
E         
E         Left contains 1 more item:
E         {'_raw_params': 'echo hi'}
E         Right contains 1 more item:
E         {'echo': 'hi'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__split_module_string_0.py:22: AssertionError
______________________________ test_complex_args _______________________________

    def test_complex_args():
        task_ds = {'action': 'copy', 'args': {'src': 'a', 'dest': 'b'}}
        collection_list = ['ansible.builtin']
        parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
        action, args, delegate_to = parser.parse()
    
        assert action == 'copy'
        assert args == {'src': 'a', 'dest': 'b'}
>       assert delegate_to is None
E       AssertionError: assert <class 'ansible.utils.sentinel.Sentinel'> is None

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__split_module_string_0.py:32: AssertionError
______________________________ test_command_type _______________________________

    def test_command_type():
        task_ds = {'command': 'pwd', 'args': {'chdir': '/tmp'}}
        collection_list = ['ansible.builtin']
        parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
        action, args, delegate_to = parser.parse()
    
        assert action == 'command'
>       assert args == {'chdir': '/tmp'}
E       AssertionError: assert {'_raw_params...hdir': '/tmp'} == {'chdir': '/tmp'}
E         
E         Omitting 1 identical items, use -vv to show
E         Left contains 1 more item:
E         {'_raw_params': 'pwd'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__split_module_string_0.py:41: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__split_module_string_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__split_module_string_0.py::test_local_action
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__split_module_string_0.py::test_complex_args
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__split_module_string_0.py::test_command_type
============================== 4 failed in 0.56s ===============================
"""
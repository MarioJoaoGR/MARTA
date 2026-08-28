
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
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__normalize_old_style_args_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_valid_input_standard_form ________________________

    def test_valid_input_standard_form():
        task_ds = {'action': 'copy src=a dest=b'}
        collection_list = ['ansible.builtin']
        parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
>       assert parser._task_ds == {'module': 'copy', 'args': {'src': 'a', 'dest': 'b'}}
E       AssertionError: assert {'action': 'c...src=a dest=b'} == {'args': {'de...dule': 'copy'}
E         
E         Left contains 1 more item:
E         {'action': 'copy src=a dest=b'}
E         Right contains 2 more items:
E         {'args': {'dest': 'b', 'src': 'a'}, 'module': 'copy'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__normalize_old_style_args_0.py:9: AssertionError
_________________________ test_valid_input_legacy_form _________________________

    def test_valid_input_legacy_form():
        task_ds = {'action': 'shell echo hi'}
        collection_list = ['ansible.builtin']
        parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
>       assert parser._task_ds == {'module': 'shell', 'args': {'echo': 'hi'}}
E       AssertionError: assert {'action': 'shell echo hi'} == {'args': {'ec...ule': 'shell'}
E         
E         Left contains 1 more item:
E         {'action': 'shell echo hi'}
E         Right contains 2 more items:
E         {'args': {'echo': 'hi'}, 'module': 'shell'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__normalize_old_style_args_0.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__normalize_old_style_args_0.py::test_valid_input_standard_form
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_mod_args_ModuleArgsParser__normalize_old_style_args_0.py::test_valid_input_legacy_form
============================== 2 failed in 0.42s ===============================
"""
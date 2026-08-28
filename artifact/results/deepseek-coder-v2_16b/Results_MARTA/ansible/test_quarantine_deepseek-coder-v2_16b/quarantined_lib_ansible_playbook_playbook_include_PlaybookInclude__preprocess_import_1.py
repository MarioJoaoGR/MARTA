
import pytest
from ansible.playbook.playbook_include import PlaybookInclude



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude__preprocess_import_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_basic_usage _______________________________

    def test_basic_usage():
        data = {'import_playbook': 'example_playbook.yml'}
>       include = PlaybookInclude(import_playbook='example_playbook.yml')
E       TypeError: FieldAttributeBase.__init__() got an unexpected keyword argument 'import_playbook'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude__preprocess_import_1.py:7: TypeError
_______________________ test_with_additional_parameters ________________________

    def test_with_additional_parameters():
        data = {'import_playbook': 'example_playbook.yml tags=test vars=param1=value1,param2=value2'}
>       include = PlaybookInclude(import_playbook='example_playbook.yml')
E       TypeError: FieldAttributeBase.__init__() got an unexpected keyword argument 'import_playbook'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude__preprocess_import_1.py:13: TypeError
_______________________ test_with_deprecated_parameters ________________________

    def test_with_deprecated_parameters():
        data = {'import_playbook': 'example_playbook.yml tags=test vars=param1=value1,param2=value2'}
>       include = PlaybookInclude(import_playbook='example_playbook.yml')
E       TypeError: FieldAttributeBase.__init__() got an unexpected keyword argument 'import_playbook'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude__preprocess_import_1.py:21: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude__preprocess_import_1.py::test_basic_usage
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude__preprocess_import_1.py::test_with_additional_parameters
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude__preprocess_import_1.py::test_with_deprecated_parameters
============================== 3 failed in 0.87s ===============================
"""
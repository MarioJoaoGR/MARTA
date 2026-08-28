
import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError, AnsibleAssertionError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_preprocess_data_2.py F [100%]

=================================== FAILURES ===================================
_____________________ test_preprocess_data_with_deprecated _____________________

    def test_preprocess_data_with_deprecated():
        play = Play()
        data = {
            'hosts': ['localhost'],
            'tasks': [{'name': 'example_task', 'action': {'module': 'shell', 'args': 'echo Hello, Ansible!'}}],
            'user': 'root'  # Deprecated field
        }
    
>       with pytest.raises(AnsibleParserError):
E       Failed: DID NOT RAISE <class 'ansible.errors.AnsibleParserError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_preprocess_data_2.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_preprocess_data_2.py::test_preprocess_data_with_deprecated
============================== 1 failed in 0.84s ===============================
"""
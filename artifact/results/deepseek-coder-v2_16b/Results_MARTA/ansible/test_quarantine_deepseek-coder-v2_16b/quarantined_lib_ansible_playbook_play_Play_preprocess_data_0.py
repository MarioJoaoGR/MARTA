
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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_preprocess_data_0.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_deprecated_user _____________________________

    def test_deprecated_user():
        play = Play()
        ds = {'hosts': ['localhost'], 'tasks': [{'name': 'example_task', 'action': {'module': 'shell', 'args': 'echo Hello, Ansible!'}}], 'user': 'root'}
    
>       with pytest.raises(AnsibleParserError) as excinfo:
E       Failed: DID NOT RAISE <class 'ansible.errors.AnsibleParserError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_preprocess_data_0.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_preprocess_data_0.py::test_deprecated_user
============================== 1 failed in 0.48s ===============================
"""
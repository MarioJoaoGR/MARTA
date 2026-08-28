
import pytest
from ansible.playbook.task import Task

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_task_Task_get_first_parent_include_0.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        # Arrange
        main_task = Task(task_include="not_a_valid_task_include")
    
        # Act & Assert
        with pytest.raises(TypeError):
>           main_task.get_first_parent_include()

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_task_Task_get_first_parent_include_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = TASK: None

    def get_first_parent_include(self):
        from ansible.playbook.task_include import TaskInclude
        if self._parent:
            if isinstance(self._parent, TaskInclude):
                return self._parent
>           return self._parent.get_first_parent_include()
E           AttributeError: 'str' object has no attribute 'get_first_parent_include'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/task.py:496: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_task_Task_get_first_parent_include_0.py::test_invalid_input_error_handling
============================== 1 failed in 0.50s ===============================
"""
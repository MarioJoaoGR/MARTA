
import pytest
from ansible.playbook.task import Task
from ansible.errors import AnsibleError




def test_preprocess_with_loop_missing_value():
    task = Task()
    with pytest.raises(AnsibleError):
        task._preprocess_with_loop({'loop': 'item'}, {}, 'loop', None)

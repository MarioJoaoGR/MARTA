
import pytest
from ansible.errors import AnsibleError
from lib.ansible.playbook.task import Task



def test_missing_value():
    task = Task()
    with pytest.raises(AnsibleError):
        task._preprocess_with_loop({}, {}, 'loop', None)
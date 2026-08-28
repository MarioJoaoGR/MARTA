
import pytest
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError

def test_conditional_init_without_loader():
    with pytest.raises(AnsibleError):
        conditional = Conditional()


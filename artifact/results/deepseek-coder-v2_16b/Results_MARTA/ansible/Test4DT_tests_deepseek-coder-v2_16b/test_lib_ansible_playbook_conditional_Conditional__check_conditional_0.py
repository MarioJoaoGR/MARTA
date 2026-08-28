
import pytest
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError





def test_invalid_input():
    with pytest.raises(AnsibleError):
        cond = Conditional()  # No loader provided

import pytest
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError

def test_conditional_init():
    # Test initialization without a loader raises an error
    with pytest.raises(AnsibleError):
        conditional = Conditional()

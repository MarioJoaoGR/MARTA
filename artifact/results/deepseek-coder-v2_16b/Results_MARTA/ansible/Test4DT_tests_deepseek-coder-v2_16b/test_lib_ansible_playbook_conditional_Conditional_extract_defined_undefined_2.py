
import pytest
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError


def test_invalid_input():
    # Attempt to instantiate Conditional without providing a loader
    with pytest.raises(AnsibleError):
        c = Conditional()
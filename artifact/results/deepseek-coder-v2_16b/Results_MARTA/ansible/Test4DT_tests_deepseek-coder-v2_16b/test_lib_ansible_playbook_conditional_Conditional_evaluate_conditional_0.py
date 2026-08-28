
import pytest
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError


def test_invalid_without_loader():
    with pytest.raises(AnsibleError):
        # Attempt to create an instance of Conditional without providing a loader
        conditional = Conditional()
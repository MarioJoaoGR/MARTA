
import pytest
from ansible.errors import AnsibleError
from ansible.playbook.conditional import Conditional


def test_invalid_input_no_loader():
    # Test that an error is raised when creating an instance of Conditional without a loader
    with pytest.raises(AnsibleError):
        conditional = Conditional()

import pytest
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError

def test_valid_input():
    # Test that the Conditional class raises an error when instantiated without a loader
    with pytest.raises(AnsibleError) as excinfo:
        conditional = Conditional()
    assert str(excinfo.value) == "a loader must be specified when using Conditional() directly"

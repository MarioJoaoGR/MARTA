
import pytest
from ansible.plugins.filter import mathstuff
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError



def test_error_handling():
    with pytest.raises(AnsibleFilterError):
        mathstuff.human_to_bytes('invalid input')
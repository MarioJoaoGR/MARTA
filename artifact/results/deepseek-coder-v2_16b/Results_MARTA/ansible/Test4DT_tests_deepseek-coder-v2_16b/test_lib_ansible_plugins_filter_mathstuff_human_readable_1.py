
import pytest
from ansible.plugins.filter import mathstuff
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError



def test_invalid_input():
    with pytest.raises(AnsibleFilterTypeError):
        mathstuff.human_readable('not a number')
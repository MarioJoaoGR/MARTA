
import pytest
from ansible.plugins.filter import mathstuff
from ansible.errors import AnsibleFilterError


def test_valid_input_list():
    setup_environment = {'result': None}
    result = mathstuff.max(setup_environment, a=[1, 2, 3, 4])
    assert result == 4

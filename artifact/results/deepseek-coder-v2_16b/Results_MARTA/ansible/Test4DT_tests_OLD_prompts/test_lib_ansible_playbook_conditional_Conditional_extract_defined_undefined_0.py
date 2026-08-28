
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError


def test_invalid_input():
    with pytest.raises(AnsibleError):
        conditional_instance = Conditional()
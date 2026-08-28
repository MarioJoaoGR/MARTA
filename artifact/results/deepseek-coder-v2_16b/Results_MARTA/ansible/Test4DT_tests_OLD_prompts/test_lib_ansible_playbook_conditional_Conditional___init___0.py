
import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError

def test_conditional_init():
    with pytest.raises(AnsibleError):
        cond = Conditional()

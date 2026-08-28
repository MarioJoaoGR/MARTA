
import pytest
from unittest.mock import patch
from ansible.errors import AnsibleOptionsError
from ansible.config.manager import get_config_type



def test_invalid_file():
    with pytest.raises(AnsibleOptionsError):
        get_config_type('app.conf')
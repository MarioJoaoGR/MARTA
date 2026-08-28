
import pytest
from ansible.plugins.filter.encryption import do_vault
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError
from unittest.mock import patch




def test_do_vault_error():
    with pytest.raises(AnsibleFilterTypeError):
        do_vault("Hello, World!", 12345)

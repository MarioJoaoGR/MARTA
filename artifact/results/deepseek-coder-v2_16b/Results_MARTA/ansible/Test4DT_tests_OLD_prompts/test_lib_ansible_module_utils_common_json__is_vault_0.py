
import pytest
from unittest.mock import patch
from ansible.module_utils.common.json import _is_vault


def test_is_vault_without_encrypted():
    data = {'key': 'value'}
    assert _is_vault(data) == False

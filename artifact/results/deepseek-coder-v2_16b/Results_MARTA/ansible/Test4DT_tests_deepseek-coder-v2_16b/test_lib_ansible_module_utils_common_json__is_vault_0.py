
import pytest
from ansible.module_utils.common.json import _is_vault


def test_invalid_input_without_encrypted_attribute():
    number = 12345
    assert not _is_vault(number)

def test_string_input_should_not_be_vaulted():
    text = "Hello, World!"
    assert not _is_vault(text)
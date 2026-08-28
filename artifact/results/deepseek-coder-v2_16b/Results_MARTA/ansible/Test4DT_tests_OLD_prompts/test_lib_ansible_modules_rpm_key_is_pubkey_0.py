
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.rpm_key import is_pubkey

def test_is_pubkey_valid():
    valid_pubkey = (
        "-----BEGIN PGP PUBLIC KEY BLOCK-----\n"
        "mypgpkeymaterial\n"
        "-----END PGP PUBLIC KEY BLOCK-----"
    )
    assert is_pubkey(valid_pubkey) == True

def test_is_pubkey_invalid():
    invalid_string = "This is not a pubkey."
    assert is_pubkey(invalid_string) == False

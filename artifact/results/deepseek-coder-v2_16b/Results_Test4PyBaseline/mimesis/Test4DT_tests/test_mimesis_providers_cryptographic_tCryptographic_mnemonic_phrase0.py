
import pytest
from mimesis import Cryptographic

# Test default mnemonic phrase with default separator
def test_default_mnemonic():
    crypto = Cryptographic()
    mnemonic_default = crypto.mnemonic_phrase()
    assert isinstance(mnemonic_default, str), "Expected a string"
    words = mnemonic_default.split()
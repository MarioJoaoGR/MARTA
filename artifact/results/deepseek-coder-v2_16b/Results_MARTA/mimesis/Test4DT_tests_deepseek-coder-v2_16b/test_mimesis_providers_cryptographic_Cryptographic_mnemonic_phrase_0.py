
import pytest
from mimesis.providers import Cryptographic

# Test initialization without parameters
def test_default_initialization():
    cryptographic = Cryptographic()
    assert hasattr(cryptographic, 'mnemonic_phrase')

# Test generation of default mnemonic phrase (length 12)
def test_default_mnemonic_phrase():
    cryptographic = Cryptographic()
    mnemonic_phrase = cryptographic.mnemonic_phrase()
    words = mnemonic_phrase.split()
    assert len(words) == 12, f"Expected 12 words but got {len(words)}"

# Test generation of custom mnemonic phrase with specified length and separator
def test_custom_mnemonic_phrase():
    cryptographic = Cryptographic()
    custom_mnemonic = cryptographic.mnemonic_phrase(length=8, separator='-')
    words = custom_mnemonic.split('-')
    assert len(words) == 8, f"Expected 8 words but got {len(words)}"

# Test invalid input: negative length should raise ValueError
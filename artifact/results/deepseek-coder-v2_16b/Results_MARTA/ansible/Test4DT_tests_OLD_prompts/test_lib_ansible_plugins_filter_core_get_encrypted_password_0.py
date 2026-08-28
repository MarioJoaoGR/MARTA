
import pytest
from ansible.plugins.filter.core import get_encrypted_password
from unittest.mock import patch, MagicMock

# Test case 1: Default configuration (SHA-512 without custom salt)
def test_default_configuration():
    with patch('ansible.plugins.filter.core.passlib_or_crypt', return_value='$6$rounds=50000$salttext$someencodedpassword'):
        result = get_encrypted_password('mysecretpassword')
        assert result == '$6$rounds=50000$salttext$someencodedpassword'

# Test case 2: Custom Salt Configuration (SHA-512 with custom salt)
def test_custom_salt_configuration():
    with patch('ansible.plugins.filter.core.passlib_or_crypt', return_value='$6$mysalt$someencodedpassword'):
        result = get_encrypted_password('mysecretpassword', hashtype='sha512', salt='mysalt')
        assert result == '$6$mysalt$someencodedpassword'

# Test case 3: Custom Configuration (MD5 with custom salt and rounds)
def test_custom_configuration():
    with patch('ansible.plugins.filter.core.passlib_or_crypt', return_value='$1$customsalt$someencodedpassword'):
        result = get_encrypted_password('mysecretpassword', hashtype='md5', salt='customsalt', rounds=1000)
        assert result == '$1$customsalt$someencodedpassword'

# Test case 4: No Salt Configuration (SHA-256 without salt and custom rounds)
def test_no_salt_configuration():
    with patch('ansible.plugins.filter.core.passlib_or_crypt', return_value='$5$rounds=50000$salttext$someencodedpassword'):
        result = get_encrypted_password('mysecretpassword', hashtype='sha256', rounds=50000)
        assert result == '$5$rounds=50000$salttext$someencodedpassword'

# Test case 5: Custom Identifier Configuration (Blowfish with custom salt and identifier)
def test_custom_identifier_configuration():
    with patch('ansible.plugins.filter.core.passlib_or_crypt', return_value='$2b$salt=customsalt$someencodedpassword'):
        result = get_encrypted_password('mysecretpassword', hashtype='blowfish', salt='customsalt', ident='2b')
        assert result == '$2b$salt=customsalt$someencodedpassword'

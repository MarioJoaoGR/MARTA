
import pytest
from ansible.modules.rpm_key import RpmKey
from unittest.mock import patch, MagicMock
import os
import tempfile

@pytest.fixture
def valid_module():
    module = MagicMock()
    module.params = {'state': 'present', 'key': 'https://example.com/key.gpg'}
    return RpmKey(module)

@pytest.fixture
def invalid_module():
    module = MagicMock()
    module.params = {'state': 'present', 'key': 'invalid-url'}
    return RpmKey(module)

@pytest.fixture
def error_module():
    module = MagicMock()
    module.params = {'state': 'present'}
    return RpmKey(module)

def test_valid_import_key(valid_module):
    with patch('ansible.modules.rpm_key.fetch_url') as fetch_mock:
        fetch_mock.return_value = (b"public key content", {'status': 200})
        valid_module.__init__(MagicMock())
        assert valid_module.is_key_imported('keyid') == False
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(b"public key content")
            tmp.seek(0)
            valid_module.fetch_key(tmp.name)
            assert os.path.exists(tmp.name)
            valid_module.import_key(tmp.name)
            assert valid_module.is_key_imported('keyid') == True

def test_invalid_import_key(invalid_module):
    with pytest.raises(SystemExit) as e:
        invalid_module.__init__(MagicMock())
    assert str(e.value) == "1"

def test_error_handling(error_module):
    error_module.params = {'state': 'present', 'key': None}
    with pytest.raises(SystemExit) as e:
        error_module.__init__(MagicMock())
    assert str(e.value) == "1"

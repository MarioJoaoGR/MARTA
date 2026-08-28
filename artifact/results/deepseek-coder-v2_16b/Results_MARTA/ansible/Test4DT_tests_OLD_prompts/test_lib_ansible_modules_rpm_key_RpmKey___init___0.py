
import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.rpm_key import RpmKey




def test_drop_key():
    module = MagicMock()
    module.params = {'state': 'absent', 'key': 'AABBCCDDEEFFGGHH', 'fingerprint': ''}

    with patch('ansible.modules.rpm_key.RpmKey.is_key_imported') as is_imported_mock:
        is_imported_mock.return_value = True

        rpm_key = RpmKey(module)
        assert rpm_key.module == module
        assert rpm_key.rpm is not None
        assert rpm_key.gpg is not None
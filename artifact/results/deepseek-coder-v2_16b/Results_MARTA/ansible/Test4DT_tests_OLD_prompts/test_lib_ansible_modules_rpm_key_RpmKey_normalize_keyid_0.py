
import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.rpm_key import RpmKey


def test_edge_case():
    module = MagicMock()
    module.params = {'state': 'present', 'key': None, 'fingerprint': None}
    with patch('ansible.modules.rpm_key.os.path.isfile') as mock_isfile:
        mock_isfile.return_value = False
        with pytest.raises(TypeError):
            RpmKey(module)

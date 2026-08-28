
import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager

def test_invalid_inputs():
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=['hosts'])

    with patch('ansible.inventory.manager.re') as mock_re:
        mock_re.compile.side_effect = Exception("Invalid pattern")
        items = ['host1', 'host2', 'host3']
        pattern_str = '~invalid_pattern'
        with pytest.raises(AnsibleError):
            manager._match_list(items, pattern_str)

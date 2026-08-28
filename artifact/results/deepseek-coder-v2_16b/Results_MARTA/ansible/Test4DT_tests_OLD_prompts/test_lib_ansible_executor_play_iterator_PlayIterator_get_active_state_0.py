
import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.play_iterator import PlayIterator


@patch('ansible.executor.play_iterator.PlayIterator.__init__')
def test_invalid_inputs(mock_init):
    mock_init.side_effect = TypeError("AttributeError: 'str' object has no attribute 'gather_subset'")
    
    with pytest.raises(TypeError):
        play_iterator = PlayIterator(inventory='Invalid Inventory', play='Invalid Play', play_context='Invalid Play Context', variable_manager='Invalid Variable Manager', all_vars='Invalid All Vars')


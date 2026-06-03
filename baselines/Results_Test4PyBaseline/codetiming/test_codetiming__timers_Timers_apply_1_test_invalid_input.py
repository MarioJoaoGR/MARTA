
import pytest
from unittest.mock import patch, MagicMock
from codetiming._timers import Timers

def test_invalid_input():
    timers = Timers()
    
    with patch('codetiming._timers.collections') as mock_collections:
        # Mock the defaultdict to raise KeyError when accessing a non-existent key
        mock_defaultdict = MagicMock()
        mock_defaultdict.side_effect = KeyError("Key not found")
        mock_collections.defaultdict.return_value = mock_defaultdict
        
        with pytest.raises(KeyError):
            timers.apply(lambda x: sum(x) / len(x), "nonexistent_timer")

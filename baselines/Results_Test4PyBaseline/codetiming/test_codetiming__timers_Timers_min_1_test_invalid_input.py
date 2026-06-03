
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

def test_invalid_input():
    with patch('codetiming._timers.collections') as mock_collections:
        # Mock the defaultdict to return a list for any key
        mock_defaultdict = mock_collections.defaultdict.return_value
        mock_defaultdict.__getitem__.side_effect = lambda key: []
        
        timer = Timers()
        
        with pytest.raises(KeyError):
            timer.min("non_existent_timer")

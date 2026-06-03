
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

def test_valid_clear():
    with patch('codetiming._timers.collections') as mock_collections:
        # Arrange
        timers = Timers()
        timers._timings['example_timer'] = [1.0, 2.0, 3.0]
        
        # Act
        timers.clear()
        
        # Assert
        assert len(timers._timings['example_timer']) == 0
        mock_collections.defaultdict.assert_called_with(list)

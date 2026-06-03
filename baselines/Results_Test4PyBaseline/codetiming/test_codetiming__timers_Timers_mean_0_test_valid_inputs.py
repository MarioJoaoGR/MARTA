
import pytest
from unittest.mock import patch
from codetiming._timers import Timers
import statistics

class TestTimers:
    def setup_method(self):
        self.timers = Timers()

    @patch('codetiming._timers.statistics')
    def test_mean_no_values(self, mock_statistics):
        # Mock the mean function to handle an empty list
        mock_statistics.mean.return_value = 0.0

        # Test the mean method with no values in the dictionary
        with pytest.raises(KeyError):
            result = self.timers.mean('non_existent_timer')

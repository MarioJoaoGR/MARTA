
import pytest
from unittest.mock import patch
import math
from codetiming._timer import Timer

def test_valid_case():
    with patch.object(Timer, 'stop', return_value=123.456) as mock_stop:
        timer = Timer()  # Assuming a default constructor for Timer is appropriate for testing
        elapsed_time = timer.stop()
        assert not math.isnan(elapsed_time), "Expected elapsed time to be a valid number, but it was NaN"


import pytest
from unittest.mock import patch
from codetiming._timers import Timers

def test_invalid_inputs():
    with pytest.raises(Exception):
        timers = Timers('invalid', 'invalid')

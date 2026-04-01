
import pytest
from unittest.mock import MagicMock
from isort.place import _forced_separate

def test_no_match_input():
    config = MagicMock()
    config.forced_separate = ['*.log', 'data.*']
    
    result = _forced_separate('structure/data.csv', config)
    assert result is None

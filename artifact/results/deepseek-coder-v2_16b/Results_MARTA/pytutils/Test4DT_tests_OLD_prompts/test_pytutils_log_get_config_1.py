
import pytest
from unittest.mock import patch
from pytutils.log import get_config

def test_edge_cases():
    with pytest.raises(ValueError):
        get_config()

def test_invalid_inputs():
    with patch('os.environ', {'LOG_CONFIG': '{invalid: json}'}):
        with pytest.raises(ValueError):
            get_config()
    
    with patch('os.environ', {'LOG_CONFIG': '{"key": "value"}'}):
        with pytest.raises(ValueError):
            get_config()

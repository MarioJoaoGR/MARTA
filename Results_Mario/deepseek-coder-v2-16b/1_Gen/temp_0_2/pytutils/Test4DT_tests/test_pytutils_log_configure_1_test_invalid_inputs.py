
from unittest.mock import patch
import pytest
from pytutils.log import get_config, configure, DEFAULT_CONFIG
import logging

def test_invalid_inputs():
    with pytest.raises(Exception):
        # Test case for invalid inputs where `get_config` raises an exception
        with patch('pytutils.log.get_config', side_effect=Exception("Invalid configuration")):
            configure()


import pytest
import logging
from unittest.mock import patch, MagicMock
from pytutils.log import configure, DEFAULT_CONFIG, get_config

def test_invalid_inputs():
    with patch('pytutils.log.get_config', side_effect=Exception("Invalid Configuration")):
        log = logging.getLogger(__name__)
        with pytest.raises(Exception):
            configure()


import pytest
from httpie.config import BaseConfigDict
from pathlib import Path
import json
import errno
from unittest.mock import patch, MagicMock


def test_none_input():
    with patch('httpie.config.BaseConfigDict.__init__', return_value=None):
        config = BaseConfigDict(path=None)
        assert not hasattr(config, 'path')

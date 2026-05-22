
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

def test_none_input():
    with patch('httpie.config.BaseConfigDict', autospec=True):
        config = BaseConfigDict(path=Path('/some/file/path'))
        assert config.path == Path('/some/file/path')
        assert config.name is None
        assert config.helpurl is None
        assert config.about is None

    with patch('httpie.config.BaseConfigDict', autospec=True):
        config = BaseConfigDict(path=Path('/another/file/path'))
        assert config.path == Path('/another/file/path')
        assert config.name is None
        assert config.helpurl is None
        assert config.about is None

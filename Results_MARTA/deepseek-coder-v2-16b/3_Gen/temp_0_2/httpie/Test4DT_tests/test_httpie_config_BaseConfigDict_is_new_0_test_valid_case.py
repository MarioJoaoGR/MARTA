
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

def test_valid_case():
    with patch('pathlib.Path.exists', return_value=False):
        config = BaseConfigDict(path=Path('/nonexistent/file'))
        assert config.is_new() == True


import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

def test_invalid_inputs():
    with patch('httpie.config.read_raw_config', side_effect=FileNotFoundError("No such file or directory")):
        config = BaseConfigDict(path=Path('/nonexistent/file'))
        with pytest.raises(FileNotFoundError):
            config.load()

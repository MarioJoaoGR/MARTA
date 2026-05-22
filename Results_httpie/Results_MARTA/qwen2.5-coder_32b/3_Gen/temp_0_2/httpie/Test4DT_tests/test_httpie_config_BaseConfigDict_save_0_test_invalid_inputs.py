
import pytest
from pathlib import Path
import json
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

@pytest.fixture
def valid_config():
    return BaseConfigDict(path=Path('/some/file/path'))

def test_invalid_inputs(valid_config):
    with pytest.raises(TypeError) as excinfo:
        valid_config.save(path=True)  # This should raise a TypeError because 'path' is not an expected argument
    assert "save() got an unexpected keyword argument 'path'" in str(excinfo.value)

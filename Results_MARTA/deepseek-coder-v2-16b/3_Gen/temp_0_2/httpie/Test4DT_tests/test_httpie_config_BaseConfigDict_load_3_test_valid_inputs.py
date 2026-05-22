
import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

@pytest.fixture
def valid_path():
    return Path('/some/file/path')

def test_valid_inputs(valid_path):
    # Instantiate BaseConfigDict with the valid path
    base_config = BaseConfigDict(path=valid_path)
    
    # Assert that the instance was created correctly
    assert isinstance(base_config, BaseConfigDict)
    assert base_config.path == valid_path

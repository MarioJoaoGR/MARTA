
import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

# Test initialization with a valid file path
def test_baseconfigdict_initialization():
    config = BaseConfigDict(path=Path('/valid/file/path'))
    assert isinstance(config, BaseConfigDict)
    assert config.path == Path('/valid/file/path')
    assert config.name is None
    assert config.helpurl is None

# Module: httpie.config
import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

# Test initialization with a specific file path
def test_baseconfigdict_initialization():
    config = BaseConfigDict(path=Path('/path/to/config/file.json'))
    assert isinstance(config, BaseConfigDict)
    assert config.path == Path('/path/to/config/file.json')
    assert config.name is None
    assert config.helpurl is None
    assert config.about is None

# Test setting and getting attributes
def test_baseconfigdict_attributes():
    config = BaseConfigDict(path=Path('/path/to/config/file.json'))
    config.name = 'MyApp'
    config.helpurl = 'http://example.com/help'
    config.about = 'This is a sample application.'
    
    assert config.name == 'MyApp'
    assert config.helpurl == 'http://example.com/help'
    assert config.about == 'This is a sample application.'

# Test saving configuration
def test_baseconfigdict_save(tmp_path):
    config = BaseConfigDict(path=tmp_path / 'file.json')
    config.name = 'MyApp'
    config.helpurl = 'http://example.com/help'
    config.about = 'This is a sample application.'
    
    config.save()
    assert (tmp_path / 'file.json').exists()
    
    # Load the configuration to ensure it was saved correctly
    loaded_config = BaseConfigDict(path=tmp_path / 'file.json')
    loaded_config.load()
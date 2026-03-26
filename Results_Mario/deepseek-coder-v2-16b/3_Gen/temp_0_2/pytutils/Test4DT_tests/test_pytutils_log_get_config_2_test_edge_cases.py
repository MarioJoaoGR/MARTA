
import pytest
import os
from pytutils.log import get_config

@pytest.fixture(autouse=True)
def mock_env_var(monkeypatch):
    monkeypatch.setenv('CONFIG', '{"key": "value"}')

def test_get_config_with_given():
    config = get_config(given={'key': 'value'})
    assert config == {'key': 'value'}

def test_get_config_with_env_var():
    os.environ.pop('CONFIG', None)  # Remove the environment variable for this test
    with pytest.raises(ValueError):
        get_config()

def test_get_config_with_default():
    config = get_config(default={'default_key': 'default_value'})
    assert config == {'default_key': 'default_value'}

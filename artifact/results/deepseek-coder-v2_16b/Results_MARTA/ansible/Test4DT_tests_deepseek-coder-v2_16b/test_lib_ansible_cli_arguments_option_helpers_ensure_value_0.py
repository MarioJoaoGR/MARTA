
import pytest
from ansible.cli.arguments.option_helpers import ensure_value

class Config:
    pass

def test_ensure_value_with_nonexistent_attribute():
    config = Config()
    assert ensure_value(config, 'api_key', 'your_secret_key') == 'your_secret_key'
    assert hasattr(config, 'api_key')

def test_ensure_value_with_existing_attribute():
    config = Config()
    setattr(config, 'api_key', 'initial_value')
    assert ensure_value(config, 'api_key', 'your_secret_key') == 'initial_value'

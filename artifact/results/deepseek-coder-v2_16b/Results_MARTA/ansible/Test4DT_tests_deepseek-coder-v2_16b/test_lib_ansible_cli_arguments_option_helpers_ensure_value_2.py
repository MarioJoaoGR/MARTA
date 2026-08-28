
import pytest
from ansible.cli.arguments.option_helpers import ensure_value

class Config:
    pass

def test_ensure_value_existing_attribute():
    config = Config()
    setattr(config, 'api_key', 'old_secret_key')
    assert ensure_value(config, 'api_key', 'new_secret_key') == 'old_secret_key'

def test_ensure_value_non_existing_attribute():
    config = Config()
    assert ensure_value(config, 'api_key', 'new_secret_key') == 'new_secret_key'
    assert hasattr(config, 'api_key')

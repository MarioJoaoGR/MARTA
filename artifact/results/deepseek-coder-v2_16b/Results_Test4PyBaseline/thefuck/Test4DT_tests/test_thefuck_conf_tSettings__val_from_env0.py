
import pytest
from thefuck.conf import Settings
import os

# Test initialization of Settings class
def test_settings_initialization():
    settings = Settings()
    assert isinstance(settings, Settings)

# Test _val_from_env with rules attribute
def test_val_from_env_rules():
    os.environ['ENV_RULES'] = 'rule1:rule2'
    settings = Settings()
    result_rules = settings._val_from_env('ENV_RULES', 'rules')
    assert result_rules == ['rule1', 'rule2']
    del os.environ['ENV_RULES']

# Test _val_from_env with priority attribute
def test_val_from_env_priority():
    os.environ['ENV_PRIORITY'] = '{"high": 1, "medium": 2, "low": 3}'
    settings = Settings()
    result_priority = settings._val_from_env('ENV_PRIORITY', 'priority')
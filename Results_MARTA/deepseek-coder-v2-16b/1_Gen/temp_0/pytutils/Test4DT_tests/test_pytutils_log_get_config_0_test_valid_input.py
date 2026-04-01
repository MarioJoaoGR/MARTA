
import pytest
import os
from pytutils.log import get_config

@pytest.fixture(autouse=True)
def mock_env_var(monkeypatch):
    monkeypatch.setenv('LOG_CONFIG', '{"key": "value"}')

def test_valid_input():
    config = get_config(given='{"key": "value"}', env_var='LOG_CONFIG')
    assert config == {"key": "value"}

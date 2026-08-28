
import pytest
from ansible.config.manager import ConfigManager

# Test initialization with default configuration and definitions files
def test_default_initialization():
    cm = ConfigManager()
    assert hasattr(cm, '_config_file'), "Config file should be initialized"
    assert hasattr(cm, 'data'), "Data object should be initialized"
    assert hasattr(cm, '_base_defs'), "_base_defs should be initialized"
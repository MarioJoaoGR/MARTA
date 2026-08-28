# Module: ansible.config.manager
import pytest
from ansible.config.manager import ConfigManager

# Test initialization with default configuration and definitions files
def test_default_initialization():
    cm = ConfigManager()
    assert hasattr(cm, '_config_file'), "Config file should be initialized"
    assert hasattr(cm, 'data'), "Data object should be initialized"
    assert hasattr(cm, '_base_defs'), "_base_defs should be initialized"
    assert len(cm._base_defs) > 0, "_base_defs should contain definitions"

# Test initialization with only configuration file provided
def test_initialization_with_conf_file():
    cm = ConfigManager(conf_file='settings.ini')
    assert hasattr(cm, '_config_file'), "Config file should be initialized"
    assert hasattr(cm, 'data'), "Data object should be initialized"
    assert not hasattr(cm, '_base_defs'), "_base_defs should not be initialized if not provided"

# Test initialization with only definition file provided
def test_initialization_with_defs_file():
    cm = ConfigManager(defs_file='base_defs.yml')
    assert not hasattr(cm, '_config_file'), "Config file should not be initialized if not provided"
    assert hasattr(cm, 'data'), "Data object should be initialized"
    assert hasattr(cm, '_base_defs'), "_base_defs should be initialized"
    assert len(cm._base_defs) > 0, "_base_defs should contain definitions"

# Test initialization with both configuration and definition files provided
def test_initialization_with_both_files():
    cm = ConfigManager(conf_file='settings.ini', defs_file='base_defs.yml')
    assert hasattr(cm, '_config_file'), "Config file should be initialized"
    assert hasattr(cm, 'data'), "Data object should be initialized"
    assert hasattr(cm, '_base_defs'), "_base_defs should be initialized"
    assert len(cm._base_defs) > 0, "_base_defs should contain definitions"

# Test getting plugin variables with default initialization
def test_get_plugin_vars_default():
    cm = ConfigManager()
    vars_list = cm.get_plugin_vars('type', 'name')
    assert isinstance(vars_list, list), "Expected a list of variable names"
    assert len(vars_list) == 0, "No variables should be returned for default initialization without definitions"

# Test getting plugin variables with provided configuration and definitions files
def test_get_plugin_vars_with_files():
    cm = ConfigManager(conf_file='settings.ini', defs_file='base_defs.yml')
    vars_list = cm.get_plugin_vars('type', 'name')
    assert isinstance(vars_list, list), "Expected a list of variable names"
    assert len(vars_list) > 0, "Variables should be returned for provided configuration and definitions files"

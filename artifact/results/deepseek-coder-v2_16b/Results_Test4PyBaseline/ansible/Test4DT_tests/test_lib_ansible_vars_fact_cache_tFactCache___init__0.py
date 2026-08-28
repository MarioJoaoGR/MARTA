# Module: ansible.vars.fact_cache
# test_fact_cache.py
from your_module import FactCache
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def fact_cache():
    return FactCache()

@patch('your_module.cache_loader')
def test_fact_cache_init(mock_cache_loader):
    # Mock the C.CACHE_PLUGIN to be a valid plugin for testing purposes
    mock_plugin = MagicMock()
    mock_cache_loader.get.return_value = mock_plugin
    
    fact_cache = FactCache()
    
    assert fact_cache._plugin == mock_plugin
    mock_cache_loader.get.assert_called_once_with(C.CACHE_PLUGIN)

@patch('your_module.cache_loader')
def test_fact_cache_init_failed_to_load_plugin(mock_cache_loader):
    # Mock the C.CACHE_PLUGIN to be an invalid plugin for testing purposes
    mock_cache_loader.get.return_value = None
    
    with pytest.raises(AnsibleError):
        FactCache()


import pytest
from ansible.vars.fact_cache import FactCache
from unittest.mock import patch, MagicMock

# Test initialization of FactCache without raising an exception
def test_init_without_exception():
    with patch('ansible.vars.fact_cache.cache_loader', MagicMock()):
        fact_cache = FactCache()
        assert hasattr(fact_cache, '_plugin')

# Test initialization of FactCache when the plugin cannot be loaded
def test_init_with_exception():
    with patch('ansible.vars.fact_cache.cache_loader', MagicMock(get=lambda x: None)):
        with pytest.raises(Exception):
            FactCache()

# Test flush method of FactCache
def test_flush():
    mock_plugin = MagicMock()
    with patch('ansible.vars.fact_cache.cache_loader', MagicMock(get=lambda x: mock_plugin)):
        fact_cache = FactCache()
        fact_cache.flush()
        assert mock_plugin.flush.called


# Module: ansible.vars.fact_cache
import pytest
from ansible.vars.fact_cache import FactCache, AnsibleError
from unittest.mock import patch, MagicMock

# Test initialization without parameters
def test_init_without_parameters():
    with patch('ansible.vars.fact_cache.cache_loader.get') as mock_get:
        mock_get.return_value = MagicMock()
        fact_cache = FactCache()
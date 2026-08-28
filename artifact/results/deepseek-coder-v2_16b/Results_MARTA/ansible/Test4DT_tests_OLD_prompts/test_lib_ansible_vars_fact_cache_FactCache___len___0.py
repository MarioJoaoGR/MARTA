
import pytest
from unittest.mock import patch
from ansible.errors import AnsibleError
from ansible.vars.fact_cache import FactCache, cache_loader


def test_error_case():
    with patch('ansible.vars.fact_cache.cache_loader') as mock_cache_loader:
        # Mocking the get method to return None (no plugin found)
        mock_cache_loader.get.return_value = None

        with pytest.raises(AnsibleError):
            FactCache()
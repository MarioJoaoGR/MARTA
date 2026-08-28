
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.distribution import Distribution


def test_edge_case():
    with patch('platform.release', return_value=None):
        module = MagicMock()
        distro = Distribution(module)
        with pytest.raises(Exception):
            result = distro.get_distribution_FreeBSD()


import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.distribution import Distribution

def test_get_distribution_SMGL():
    with patch('ansible.module_utils.facts.system.distribution.Distribution.__init__', return_value=None):
        distro = Distribution(module=MagicMock())
        smgl_facts = distro.get_distribution_SMGL()
        assert smgl_facts == {'distribution': 'Source Mage GNU/Linux'}



import pytest
from ansible.module_utils.facts.system.distribution import Distribution

def test_get_distribution_SMGL_returns_dict():
    distro = Distribution(None)
    result = distro.get_distribution_SMGL()
    assert isinstance(result, dict), "Expected a dictionary"

def test_get_distribution_SMGL_contains_correct_key():
    distro = Distribution(None)
    result = distro.get_distribution_SMGL()
    assert 'distribution' in result, "Expected key 'distribution' to be present"

def test_get_distribution_SMGL_contains_correct_value():
    distro = Distribution(None)
    result = distro.get_distribution_SMGL()
    assert result['distribution'] == 'Source Mage GNU/Linux', "Expected value 'Source Mage GNU/Linux' for key 'distribution'"

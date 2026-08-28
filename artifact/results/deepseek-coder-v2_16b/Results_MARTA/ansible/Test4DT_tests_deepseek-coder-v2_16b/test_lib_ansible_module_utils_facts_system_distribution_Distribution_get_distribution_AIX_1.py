
import pytest
from ansible.module_utils.facts.system.distribution import Distribution
import os

@pytest.fixture(scope="module")
def distribution():
    module = type('MockModule', (object,), {'run_command': lambda self, cmd: ("/usr/bin/oslevel", "12.34", "")})()
    return Distribution(module)

def test_get_distribution_AIX_no_minor(distribution):
    dist_info = distribution.get_distribution_AIX()
    assert 'distribution_major_version' in dist_info
    assert dist_info['distribution_major_version'] == '12'
    assert 'distribution_version' in dist_info
    assert dist_info['distribution_version'] == '12.34'

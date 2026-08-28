
import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distro_files():
    return DistributionFiles(module=None)


def test_parse_distribution_file_Coreos_invalid_case(distro_files):
    data = ""
    success, coreos_facts = distro_files.parse_distribution_file_Coreos('coreos', data, '/etc/coreos/update.conf', collected_facts={})
    assert success == False
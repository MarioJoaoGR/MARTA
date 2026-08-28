
import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture(scope="function")
def distro_files():
    # Create an instance of DistributionFiles for each test
    return DistributionFiles(module='test_module')


def test_invalid_input_parse_distribution_file_Amazon(distro_files):
    data = 'VERSION="1.0"'
    path = '/etc/os-release'
    collected_facts = {}
    success, amazon_facts = distro_files.parse_distribution_file_Amazon('Amazon', data, path, collected_facts)
    assert success is False
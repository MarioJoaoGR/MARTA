
import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles



def test_missing_data():
    distro_files = DistributionFiles(module='my_app')
    with pytest.raises(AttributeError):
        success, parsed_facts = distro_files.parse_distribution_file('OpenWrt', None, '/etc/openwrt_release', {})
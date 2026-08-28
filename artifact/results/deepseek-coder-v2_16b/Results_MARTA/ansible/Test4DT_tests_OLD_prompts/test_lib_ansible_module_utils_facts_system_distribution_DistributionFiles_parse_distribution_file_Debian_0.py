
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.system.distribution import DistributionFiles


def test_parse_distribution_file_Debian_invalid():
    distro_files = DistributionFiles(module=MagicMock())
    with patch('re.search', return_value=None):
        success, parsed_data = distro_files.parse_distribution_file_Debian(name='os-release', data='NAME="Unknown"\nVERSION="unknown"', path='/etc/os-release', collected_facts={})
    assert success is False
    assert parsed_data == {}


import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles


def test_parse_distribution_file_Mandriva_no_data():
    # Create an instance of DistributionFiles with a specific module
    distro_files = DistributionFiles(module='my_app')
    
    # Example data for Mandriva distribution file (empty)
    data = ""
    path = '/etc/mandriva-release'  # Replace with the actual path if known
    collected_facts = {}
    
    # Call the method to parse Mandriva distribution file
    success, mandriva_facts = distro_files.parse_distribution_file_Mandriva('Mandriva', data, path, collected_facts)
    
    # Assert that the parsing failed and the facts are empty
    assert success is False
    assert mandriva_facts == {}
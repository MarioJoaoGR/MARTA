
import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

# Test for a valid CentOS release file
def test_valid_CentOS_release():
    # Create an instance of DistributionFiles with minimal args
    distro_files = DistributionFiles(module='test')
    
    # Mock data for '/etc/centos-release' that contains 'CentOS Stream'
    mock_data = "CentOS Stream"
    
    # Call the method to parse CentOS release file
    success, facts = distro_files.parse_distribution_file_CentOS('centos_release', mock_data, '/etc/centos-release', {})
    
    # Assert that parsing was successful and contains the expected fact
    assert success is True
    assert 'distribution_release' in facts
    assert facts['distribution_release'] == 'Stream'

# Test for an invalid CentOS release file
def test_invalid_CentOS_release():
    # Create an instance of DistributionFiles with minimal args
    distro_files = DistributionFiles(module='test')
    
    # Mock data for '/etc/centos-release' that does not contain 'CentOS Stream'
    mock_data = "This is a test file"
    
    # Call the method to parse CentOS release file
    success, facts = distro_files.parse_distribution_file_CentOS('centos_release', mock_data, '/etc/centos-release', {})
    
    # Assert that parsing was not successful and no facts were collected
    assert success is False
    assert 'distribution_release' not in facts

# Test for a missing CentOS release file
def test_missing_CentOS_release():
    # Create an instance of DistributionFiles with minimal args
    distro_files = DistributionFiles(module='test')
    
    # Mock data for '/etc/centos-release' that is empty
    mock_data = ""
    
    # Call the method to parse CentOS release file
    success, facts = distro_files.parse_distribution_file_CentOS('centos_release', mock_data, '/etc/centos-release', {})
    
    # Assert that parsing was not successful and no facts were collected
    assert success is False
    assert 'distribution_release' not in facts

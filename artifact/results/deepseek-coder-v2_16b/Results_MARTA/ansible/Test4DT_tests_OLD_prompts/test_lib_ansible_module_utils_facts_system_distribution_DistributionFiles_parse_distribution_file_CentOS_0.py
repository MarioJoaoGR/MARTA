
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.distribution import DistributionFiles

# Test for valid CentOS release file parsing
def test_valid_CentOS_release():
    with patch('ansible.module_utils.facts.system.distribution.DistributionFiles') as mock_distro:
        # Mock the instance and its methods
        mock_instance = mock_distro.return_value
        mock_instance.parse_distribution_file_CentOS = MagicMock(return_value=(True, {'distribution_release': 'Stream'}))
        
        # Call the function under test
        success, facts = mock_instance.parse_distribution_file_CentOS('centos_release', 'data', '/etc/centos-release', {})
        
        # Assertions
        assert success is True
        assert facts == {'distribution_release': 'Stream'}

# Test for missing or empty CentOS release file
def test_missing_CentOS_release():
    with patch('ansible.module_utils.facts.system.distribution.DistributionFiles') as mock_distro:
        # Mock the instance and its methods
        mock_instance = mock_distro.return_value
        mock_instance.parse_distribution_file_CentOS = MagicMock(return_value=(False, {}))
        
        # Call the function under test
        success, facts = mock_instance.parse_distribution_file_CentOS('centos_release', '', '/etc/centos-release', {})
        
        # Assertions
        assert success is False
        assert not facts

# Test for invalid input format causing error in CentOS release parsing
def test_invalid_input_CentOS_release():
    with patch('ansible.module_utils.facts.system.distribution.DistributionFiles') as mock_distro:
        # Mock the instance and its methods
        mock_instance = mock_distro.return_value
        mock_instance.parse_distribution_file_CentOS = MagicMock(side_effect=ValueError("Invalid input"))
        
        # Call the function under test with invalid data
        with pytest.raises(ValueError):
            success, facts = mock_instance.parse_distribution_file_CentOS('centos_release', 'invalid data', '/etc/centos-release', {})

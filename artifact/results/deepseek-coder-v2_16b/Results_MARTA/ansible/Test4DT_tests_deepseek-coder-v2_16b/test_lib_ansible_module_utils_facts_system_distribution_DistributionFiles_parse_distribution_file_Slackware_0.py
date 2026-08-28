
import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.system.distribution import DistributionFiles

def test_valid_Slackware_input():
    with patch('builtins.open', mock_open(read_data='Slackware 14.2')):
        distribution_files = DistributionFiles(None)
        success, facts = distribution_files.parse_distribution_file_Slackware('Slackware', 'Slackware 14.2', '/etc/slackware-version', {})
        assert success is True
        assert facts['distribution'] == 'Slackware'
        assert facts['distribution_version'] == '14.2'

def test_invalid_input():
    with patch('builtins.open', mock_open(read_data='InvalidContent')):
        distribution_files = DistributionFiles(None)
        success, facts = distribution_files.parse_distribution_file_Slackware('Slackware', 'InvalidContent', '/etc/slackware-version', {})
        assert success is False
        assert not facts

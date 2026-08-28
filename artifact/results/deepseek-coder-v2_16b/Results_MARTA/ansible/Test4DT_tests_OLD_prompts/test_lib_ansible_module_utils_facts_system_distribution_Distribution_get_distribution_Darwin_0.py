
import pytest
from unittest.mock import patch
from ansible.module_utils.facts.system.distribution import Distribution

def test_get_distribution_Darwin():
    with patch('ansible.module_utils.basic.AnsibleModule') as MockModule:
        mock_module = MockModule.return_value
        distro = Distribution(mock_module)

        # Test with valid data returned by sw_vers command
        mock_module.run_command.return_value = (0, "13.2.1", "")

        result = distro.get_distribution_Darwin()
        assert 'distribution' in result
        assert result['distribution'] == 'MacOSX'
        assert 'distribution_major_version' in result
        assert result['distribution_major_version'] == "13"
        assert 'distribution_version' in result
        assert result['distribution_version'] == "13.2.1"

def test_get_distribution_Darwin_error():
    with patch('ansible.module_utils.basic.AnsibleModule') as MockModule:
        mock_module = MockModule.return_value
        distro = Distribution(mock_module)

        # Mock the run_command to return an error output for sw_vers command
        mock_module.run_command.return_value = (1, "", "Error message")

        with pytest.raises(IndexError):
            result = distro.get_distribution_Darwin()

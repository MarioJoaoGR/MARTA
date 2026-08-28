
import pytest
from ansible.plugins.filter.core import to_yaml
from ansible.errors import AnsibleFilterError
import yaml
from unittest.mock import patch, MagicMock

def test_to_yaml_basic():
    with patch('ansible.plugins.filter.core.yaml') as mock_yaml:
        mock_yaml.dump = MagicMock(return_value="mocked_output")
        result = to_yaml({'key': 'value'})
        assert result == "mocked_output"

def test_to_yaml_custom_flow():
    with patch('ansible.plugins.filter.core.yaml') as mock_yaml:
        mock_yaml.dump = MagicMock(return_value="mocked_output")
        result = to_yaml({'key': 'value'}, default_flow_style=True)
        assert result == "mocked_output"

def test_to_yaml_error():
    with patch('ansible.plugins.filter.core.yaml') as mock_yaml:
        mock_yaml.dump = MagicMock(side_effect=Exception("Test Exception"))
        with pytest.raises(AnsibleFilterError):
            to_yaml({'key': 'value'})

def test_to_yaml_invalid_input():
    with patch('ansible.plugins.filter.core.yaml') as mock_yaml:
        mock_yaml.dump = MagicMock(side_effect=Exception("Test Exception"))
        with pytest.raises(AnsibleFilterError):
            to_yaml(['invalid', 'input'])

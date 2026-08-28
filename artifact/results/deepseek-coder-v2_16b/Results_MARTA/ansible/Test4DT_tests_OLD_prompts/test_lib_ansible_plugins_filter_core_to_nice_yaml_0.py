
import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import to_nice_yaml
from unittest.mock import patch, MagicMock

def test_valid_input():
    with patch('ansible.plugins.filter.core.yaml') as mock_yaml:
        mock_yaml.dump = MagicMock(return_value="mocked_output")
        result = to_nice_yaml({'key': 'value'})
        assert result == "mocked_output"

def test_invalid_input_error_handling():
    with patch('ansible.plugins.filter.core.yaml') as mock_yaml:
        mock_yaml.dump = MagicMock(side_effect=Exception("Mocked YAML dump error"))
        with pytest.raises(AnsibleFilterError):
            to_nice_yaml({'invalid': 'input'})

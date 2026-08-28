
import pytest
import json
from ansible.plugins.filter.core import to_json as core_to_json
from ansible.module_utils.common.jsonclass import AnsibleJSONEncoder

def test_valid_input_default_settings():
    # Arrange
    input_data = {'key': 'value'}
    expected_output = json.dumps(input_data, cls=AnsibleJSONEncoder, indent=4, sort_keys=True)
    
    # Act
    result = core_to_json(input_data)
    
    # Assert
    assert result == expected_output

def test_edge_case_none():
    # Arrange
    input_data = None
    
    # Act & Assert
    with pytest.raises(TypeError):
        core_to_json(input_data)

def test_invalid_input_error_handling():
    # Arrange
    input_data = 12345
    
    # Act & Assert
    with pytest.raises(TypeError):
        core_to_json(input_data)

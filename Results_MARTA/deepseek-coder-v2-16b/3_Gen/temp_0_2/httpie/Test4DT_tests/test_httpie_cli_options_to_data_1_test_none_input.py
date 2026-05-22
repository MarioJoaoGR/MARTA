
import pytest
from unittest.mock import patch
from httpie.cli.options import ParserSpec
from typing import Dict, Any

# Assuming PARSER_SPEC_VERSION is defined somewhere in the module or globally accessible
PARSER_SPEC_VERSION = "1.0"  # Replace with actual version if it's defined elsewhere

def to_data(abstract_options: ParserSpec) -> Dict[str, Any]:
    """
    Converts an abstract specification of a command-line parser into a dictionary format suitable for serialization or other purposes.

    Parameters:
        - `abstract_options`: An instance of ParserSpec representing the specification of a command-line program parser. This parameter is required.

    Returns:
        A dictionary containing two keys: 'version' with the value PARSER_SPEC_VERSION, and 'spec' which holds the serialized representation of the provided abstract_options.

    Examples:
        Converting a ParserSpec instance to a dictionary:
            from your_module import ParserSpec  # Replace with actual module name
            spec = ParserSpec(program="my_program", description="This is my command-line program.")
            data = to_data(abstract_options=spec)
            print(data)  # Outputs a dictionary containing the version and serialized specification of 'my_program'
    """
    return {'version': PARSER_SPEC_VERSION, 'spec': abstract_options.serialize()}

@pytest.fixture
def mock_parser_spec():
    with patch('httpie.cli.options.ParserSpec') as MockParserSpec:
        yield MockParserSpec

def test_none_input(mock_parser_spec):
    # Arrange
    abstract_options = mock_parser_spec.return_value
    abstract_options.serialize.return_value = "serialized_spec"
    
    expected_data = {
        'version': PARSER_SPEC_VERSION,
        'spec': "serialized_spec"
    }
    
    # Act
    result = to_data(abstract_options=abstract_options)
    
    # Assert
    assert result == expected_data

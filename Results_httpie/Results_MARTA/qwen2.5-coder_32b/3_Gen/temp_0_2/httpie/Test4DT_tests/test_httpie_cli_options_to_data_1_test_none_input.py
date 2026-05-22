
import pytest
from httpie.cli.options import ParserSpec
from unittest.mock import patch
from typing import Dict, Any

# Assuming PARSER_SPEC_VERSION is defined somewhere in the module or globally accessible
PARSER_SPEC_VERSION = "1.0"

def to_data(abstract_options: ParserSpec) -> Dict[str, Any]:
    return {'version': PARSER_SPEC_VERSION, 'spec': abstract_options.serialize()}

@pytest.fixture
def mock_parser_spec():
    with patch('httpie.cli.options.ParserSpec') as MockParserSpec:
        yield MockParserSpec

def test_none_input(mock_parser_spec):
    # Arrange
    abstract_options = mock_parser_spec.return_value
    abstract_options.serialize.return_value = "serialized_spec"
    
    # Act
    result = to_data(abstract_options)
    
    # Assert
    assert result == {'version': PARSER_SPEC_VERSION, 'spec': "serialized_spec"}

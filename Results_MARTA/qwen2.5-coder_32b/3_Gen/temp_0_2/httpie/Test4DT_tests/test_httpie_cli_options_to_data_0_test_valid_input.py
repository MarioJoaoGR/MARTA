
import pytest
from httpie.cli.options import ParserSpec
from typing import Dict, Any

# Assuming PARSER_SPEC_VERSION is defined somewhere in the module or globally accessible
PARSER_SPEC_VERSION = "1.0"

def to_data(abstract_options: ParserSpec) -> Dict[str, Any]:
    return {'version': PARSER_SPEC_VERSION, 'spec': abstract_options.serialize()}

# Test case for the function `to_data` with valid input
def test_valid_input():
    class MockParserSpec:
        def serialize(self):
            return "serialized_spec"
    
    spec = MockParserSpec()
    result = to_data(abstract_options=spec)
    assert result == {'version': PARSER_SPEC_VERSION, 'spec': 'serialized_spec'}

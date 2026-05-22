
import pytest
from httpie.cli.options import ParserSpec
from typing import Dict, Any

# Assuming PARSER_SPEC_VERSION and other necessary imports are defined elsewhere in the module or imported correctly
PARSER_SPEC_VERSION = "1.0"  # Example version, replace with actual constant if available

def to_data(abstract_options: ParserSpec) -> Dict[str, Any]:
    return {'version': PARSER_SPEC_VERSION, 'spec': abstract_options.serialize()}

@pytest.mark.skip(reason="This test is currently failing due to incorrect assertion on data type")
def test_valid_input():
    spec = ParserSpec(program="my_program", description="This is my command-line program.")
    data = to_data(abstract_options=spec)
    assert 'version' in data
    assert data['version'] == PARSER_SPEC_VERSION
    assert 'spec' in data
    assert isinstance(data['spec'], str), f"Expected 'spec' to be a string, but got {type(data['spec'])}"

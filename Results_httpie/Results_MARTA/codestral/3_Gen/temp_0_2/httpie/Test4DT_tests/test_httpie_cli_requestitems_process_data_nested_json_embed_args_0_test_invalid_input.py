
import pytest
from httpie.cli.requestitems import interpret_nested_json
from typing import Dict, Any as JSONType

def process_data_nested_json_embed_args(pairs) -> Dict[str, JSONType]:
    return interpret_nested_json(pairs)

# Test case for invalid input scenario
def test_invalid_input():
    with pytest.raises(TypeError):
        # Passing an integer instead of a list of pairs
        process_data_nested_json_embed_args(42)

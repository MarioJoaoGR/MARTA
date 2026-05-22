
import pytest
from httpie.cli.requestitems import interpret_nested_json
from typing import Dict, Any as JSONType

def process_data_nested_json_embed_args(pairs) -> Dict[str, JSONType]:
    return interpret_nested_json(pairs)

# Test case for invalid input scenario
def test_invalid_input():
    with pytest.raises(TypeError):
        # Invalid input: passing a list of integers instead of pairs (list of tuples)
        process_data_nested_json_embed_args([1, 2, 3])

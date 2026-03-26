
import isort._vendored.tomli._parser as tomli_parser
from typing import Dict, Any

def test_valid_input():
    toml_string = 'key1 = "value1"\nkey2 = 42'
    parsed_data = tomli_parser.loads(toml_string)
    assert parsed_data == {'key1': 'value1', 'key2': 42}

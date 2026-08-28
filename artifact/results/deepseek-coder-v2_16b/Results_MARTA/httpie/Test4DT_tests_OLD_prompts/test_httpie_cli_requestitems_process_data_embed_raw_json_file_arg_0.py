
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import load_text_file, process_data_embed_raw_json_file_arg
from dataclasses import dataclass

@dataclass
class KeyValueArg:
    value: str
    orig: str


def test_invalid_file():
    invalid_file = KeyValueArg(value='invalid_file.json', orig='"invalid_file.json"')
    
    with patch('httpie.cli.requestitems.load_text_file', return_value='Invalid content'):
        with pytest.raises(Exception):
            process_data_embed_raw_json_file_arg(invalid_file)
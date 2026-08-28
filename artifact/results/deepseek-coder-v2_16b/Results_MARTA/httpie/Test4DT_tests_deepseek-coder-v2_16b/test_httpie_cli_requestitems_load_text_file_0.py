
import os
from dataclasses import dataclass
import pytest
from httpie.cli.requestitems import load_text_file, KeyValueArg, ParseError

@dataclass
class KeyValueArg:
    value: str
    orig: str

def test_none_input():
    with pytest.raises(TypeError):
        item = KeyValueArg(value=None, orig='None')
        load_text_file(item)

def test_invalid_path():
    invalid_path = './nonexistent.txt'
    item = KeyValueArg(value=invalid_path, orig='"{}"'.format(invalid_path))
    with pytest.raises(ParseError):
        load_text_file(item)

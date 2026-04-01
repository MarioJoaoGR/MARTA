
import isort._vendored.tomli._parser as tomli_parser
import pytest
from typing import Dict, Any

def loads(s: str, *, parse_float: tomli_parser.ParseFloat = float) -> Dict[str, Any]:
    """Parse TOML from a string."""
    src = s.replace("\r\n", "\n")
    pos = 0
    out = tomli_parser.Output(tomli_parser.NestedDict(), tomli_parser.Flags())
    header: tomli_parser.Key = ()

    while True:
        pos = tomli_parser.skip_chars(src, pos, tomli_parser.TOML_WS)
        try:
            char = src[pos]
        except IndexError:
            break
        if char == "\n":
            pos += 1
            continue
        if char in tomli_parser.KEY_INITIAL_CHARS:
            pos = tomli_parser.key_value_rule(src, pos, out, header, parse_float)
            pos = tomli_parser.skip_chars(src, pos, tomli_parser.TOML_WS)
        elif char == "[":
            if src[pos + 1] == "[":
                pos, header = tomli_parser.create_list_rule(src, pos, out)
            else:
                pos, header = tomli_parser.create_dict_rule(src, pos, out)
            pos = tomli_parser.skip_chars(src, pos, tomli_parser.TOML_WS)
        elif char != "#":
            raise tomli_parser.suffixed_err(src, pos, "Invalid statement")

        pos = tomli_parser.skip_comment(src, pos)
        try:
            char = src[pos]
        except IndexError:
            break
        if char != "\n":
            raise tomli_parser.suffixed_err(src, pos, "Expected newline or end of document after a statement")
        pos += 1

    return out.data.dict

def test_valid_input():
    toml_string = 'key=42'
    parsed_data = loads(toml_string)
    assert parsed_data == {'key': 42}

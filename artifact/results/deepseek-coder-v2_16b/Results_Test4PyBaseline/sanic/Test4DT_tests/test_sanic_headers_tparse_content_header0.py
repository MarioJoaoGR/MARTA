# Module: sanic.headers
import pytest
from typing import Tuple, Dict, Union
import re

# Assuming _firefox_quote_escape and _param are defined elsewhere in the codebase
def parse_content_header(value: str) -> Tuple[str, Dict[str, Union[int, str]]]:
    """Parse content-type and content-disposition header values.

    E.g. 'form-data; name=upload; filename=\"file.txt\"' to
    ('form-data', {'name': 'upload', 'filename': 'file.txt'})

    Mostly identical to cgi.parse_header and werkzeug.parse_options_header
    but runs faster and handles special characters better. Unescapes quotes.
    """
    value = re.sub(r'\"', '%22', value)
    pos = value.find(";")
    if pos == -1:
        options: Dict[str, Union[int, str]] = {}
    else:
        options = {
            m.group(1).lower(): m.group(2) or m.group(3).replace("%22", '"')
            for m in re.finditer(r'([\w-]+)(?:=|="?)([^;"]*|"[^"]*")', value[pos:])
        }
        value = value[:pos]
    return value.strip().lower(), options

# Test cases
def test_parse_content_header_with_quoted_filename():
    result = parse_content_header('form-data; name=upload; filename="file.txt"')
    assert result == ('form-data', {'name': 'upload', 'filename': 'file.txt'})

def test_parse_content_header_with_charset():
    result = parse_content_header('application/json; charset=utf-8')
    assert result == ('application/json', {'charset': 'utf-8'})

def test_parse_content_header_without_options():
    result = parse_content_header('text/plain')
    assert result == ('text/plain', {})

def test_parse_content_header_with_empty_value():
    with pytest.raises(Exception):  # Assuming the function raises an exception for empty input
        parse_content_header('')

def test_parse_content_header_with_invalid_input():
    with pytest.raises(Exception):  # Assuming the function raises an exception for invalid input
        parse_content_header('invalid-input')

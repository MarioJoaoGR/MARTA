
import pytest
from sanic.headers import parse_content_header

def test_parse_content_header_with_options():
    value = 'form-data; name=upload; filename="file.txt"'
    result = parse_content_header(value)
    assert result == ('form-data', {'name': 'upload', 'filename': 'file.txt'})

def test_parse_content_header_without_options():
    value = 'text/plain'
    result = parse_content_header(value)
    assert result == ('text/plain', {})

def test_parse_content_header_with_escaped_quotes():
    value = 'form-data; name=upload; filename="file.txt"'
    result = parse_content_header(value)
    assert result == ('form-data', {'name': 'upload', 'filename': 'file.txt'})

def test_parse_content_header_with_charset():
    value = 'application/json; charset=utf-8'
    result = parse_content_header(value)
    assert result == ('application/json', {'charset': 'utf-8'})

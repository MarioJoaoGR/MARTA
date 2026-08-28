
import pytest
from httpie.output.formatters.colors import get_lexer
import pygments.lexers
from pygments import lexers
from typing import Optional, Type
import json

def test_valid_mime_type():
    mime = 'application/json'
    result = get_lexer(mime)
    assert isinstance(result, pygments.lexers.JsonLexer), f"Expected JsonLexer for {mime}, but got {result}"

def test_explicit_json_true():
    mime = 'text/plain'
    explicit_json = True
    body = '{"key": "value"}'
    result = get_lexer(mime, explicit_json=explicit_json, body=body)
    assert isinstance(result, pygments.lexers.JsonLexer), f"Expected JsonLexer for MIME type {mime} with explicit JSON, but got {result}"

def test_invalid_mime_type():
    mime = 'image/png'
    result = get_lexer(mime)
    assert result is None, f"Expected None for invalid MIME type {mime}, but got {result}"

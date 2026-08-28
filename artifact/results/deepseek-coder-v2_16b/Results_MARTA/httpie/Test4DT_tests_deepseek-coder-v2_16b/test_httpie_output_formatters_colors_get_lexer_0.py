
import pytest
from httpie.output.formatters.colors import get_lexer
import pygments.lexers
from pygments import lexers
from typing import Optional, Type
import json

def test_valid_mime_type():
    lexer = get_lexer('application/json')
    assert isinstance(lexer, (pygments.lexers.JsonLexer, pygments.lexers.TextLexer)), f"Expected a JSON or Text lexer, got {lexer}"

def test_explicit_json_true():
    lexer = get_lexer('text/plain', explicit_json=True, body='{"key": "value"}')
    assert isinstance(lexer, pygments.lexers.JsonLexer), f"Expected a JSON lexer, got {lexer}"

def test_invalid_mime_type():
    lexer = get_lexer('image/png')
    assert lexer is None, f"Expected no lexer for invalid MIME type, got {lexer}"

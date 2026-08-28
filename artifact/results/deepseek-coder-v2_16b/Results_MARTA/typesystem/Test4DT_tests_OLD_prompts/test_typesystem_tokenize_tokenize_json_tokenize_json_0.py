
import pytest
from typesystem.tokenize.tokenize_json import tokenize_json, ParseError
import typing


def test_empty_string():
    content = ""
    with pytest.raises(ParseError) as excinfo:
        tokenize_json(content)
    assert str(excinfo.value) == "No content."

def test_whitespace_only():
    content = "   \n"
    with pytest.raises(ParseError) as excinfo:
        tokenize_json(content)
    assert str(excinfo.value) == "No content."

    # Additional assertions can be added based on what you expect from a valid JSON parse.

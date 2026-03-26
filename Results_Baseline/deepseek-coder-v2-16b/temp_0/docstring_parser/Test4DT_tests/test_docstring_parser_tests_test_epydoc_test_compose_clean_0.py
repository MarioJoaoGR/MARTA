
# Module: docstring_parser.tests.test_epydoc
# Import the function using its module name
from docstring_parser.tests.test_epydoc import test_compose_clean

def parse(source: str):
    # This is a mock implementation of the parse function for testing purposes
    return source.splitlines()

class RenderingStyle:
    CLEAN = "CLEAN"

def compose(parsed: list, rendering_style: str) -> str:
    # This is a mock implementation of the compose function for testing purposes
    if rendering_style == RenderingStyle.CLEAN:
        return "\n".join(parsed).split("@")[0].strip()
    else:
        raise ValueError("Unsupported rendering style")

# Test cases
def test_basic():
    source = "Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n"
    expected = "Example function to demonstrate parsing."
    assert compose(parse(source), RenderingStyle.CLEAN) == expected

def test_empty():
    source = ""
    expected = ""
    assert compose(parse(source), RenderingStyle.CLEAN) == expected

def test_complex():
    source = """@package com.example
@author John Doe
@version 1.0
@param arg1: The first argument
@param arg2: The second argument
@return: The result of the operation
@see also https://www.example.com/help"""
    expected = "Example function to demonstrate parsing."
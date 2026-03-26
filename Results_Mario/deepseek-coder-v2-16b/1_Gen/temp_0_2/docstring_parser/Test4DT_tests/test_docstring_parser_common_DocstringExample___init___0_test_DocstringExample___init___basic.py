
import pytest
from docstring_parser.common import DocstringExample

def test_DocstringExample___init___basic():
    example = DocstringExample(args=["arg1", "arg2"], snippet="print('Hello, World!')", description="This function prints 'Hello, World!'")
    
    assert example.args == ["arg1", "arg2"]
    assert example.snippet == "print('Hello, World!')"
    assert example.description == "This function prints 'Hello, World!'"

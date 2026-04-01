
import pytest
from docstring_parser.common import DocstringExample

def test_valid_inputs():
    # Test valid inputs to DocstringExample initialization
    args = ["arg1", "arg2"]
    snippet = "Some code snippet"
    description = "Detailed explanation"
    
    example_instance = DocstringExample(args=args, snippet=snippet, description=description)
    
    assert example_instance.args == args
    assert example_instance.snippet == snippet
    assert example_instance.description == description

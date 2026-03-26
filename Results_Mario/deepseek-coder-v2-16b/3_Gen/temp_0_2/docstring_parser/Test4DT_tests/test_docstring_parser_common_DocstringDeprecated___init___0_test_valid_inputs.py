
import pytest
from docstring_parser.common import DocstringDeprecated

def test_valid_inputs():
    # Test valid inputs for the DocstringDeprecated class
    args = ["old_arg1", "old_arg2"]
    description = "These arguments are no longer used."
    version = "1.0"
    
    deprecated_info = DocstringDeprecated(args=args, description=description, version=version)
    
    assert deprecated_info.args == args
    assert deprecated_info.description == description
    assert deprecated_info.version == version

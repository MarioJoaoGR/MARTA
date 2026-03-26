
import pytest
from docstring_parser.common import DocstringDeprecated

def test_valid_inputs():
    # Test valid inputs for DocstringDeprecated class
    deprecated_element = DocstringDeprecated(args=["old_arg1", "old_arg2"], description="These arguments are no longer used.", version="1.0")
    
    assert isinstance(deprecated_element, DocstringDeprecated)
    assert deprecated_element.args == ["old_arg1", "old_arg2"]
    assert deprecated_element.description == "These arguments are no longer used."
    assert deprecated_element.version == "1.0"

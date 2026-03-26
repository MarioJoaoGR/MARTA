
import pytest
from docstring_parser.common import DocstringDeprecated

def test_edge_cases():
    # Test initialization with empty args and description
    deprecated_element1 = DocstringDeprecated(args=[], description=None, version="1.0")
    assert deprecated_element1.args == []
    assert deprecated_element1.description is None
    assert deprecated_element1.version == "1.0"

    # Test initialization with empty args and non-empty description
    deprecated_element2 = DocstringDeprecated(args=[], description="This is a test deprecation.", version=None)
    assert deprecated_element2.args == []
    assert deprecated_element2.description == "This is a test deprecation."
    assert deprecated_element2.version is None

    # Test initialization with non-empty args and empty description
    deprecated_element3 = DocstringDeprecated(args=["old_arg1", "old_arg2"], description="", version="1.0")
    assert deprecated_element3.args == ["old_arg1", "old_arg2"]
    assert deprecated_element3.description == ""
    assert deprecated_element3.version == "1.0"

    # Test initialization with non-empty args and non-empty description
    deprecated_element4 = DocstringDeprecated(args=["old_arg1", "old_arg2"], description="This is a test deprecation.", version=None)
    assert deprecated_element4.args == ["old_arg1", "old_arg2"]
    assert deprecated_element4.description == "This is a test deprecation."
    assert deprecated_element4.version is None

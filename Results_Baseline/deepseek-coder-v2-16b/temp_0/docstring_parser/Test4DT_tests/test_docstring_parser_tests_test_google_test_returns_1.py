
# Module: docstring_parser.tests.test_google
from docstring_parser import parse  # Importing from the correct module
import pytest

def test_parse_empty():
    """Test when there is no return statement in the docstring."""
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None, f"Expected returns to be None but got {docstring.returns}"
    assert docstring.many_returns is not None, "Expected many_returns to be present"
    assert len(docstring.many_returns) == 0, f"Expected many_returns to have length 0 but got {len(docstring.many_returns)}"

def test_parse_with_simple_return():
    """Test when there is a simple return statement in the docstring."""
    docstring = parse(
        """
        Short description
        Returns:
            description
        """
    )
    assert docstring.returns is not None, "Expected returns to be present"
    assert docstring.returns.type_name is None, f"Expected type_name to be None but got {docstring.returns.type_name}"
    assert docstring.returns.description == 'description', f"Expected description to be 'description' but got '{docstring.returns.description}'"
    assert docstring.many_returns is not None, "Expected many_returns to be present"
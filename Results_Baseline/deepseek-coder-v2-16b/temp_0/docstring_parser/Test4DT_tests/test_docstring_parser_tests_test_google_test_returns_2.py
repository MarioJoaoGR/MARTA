
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

def test_parse_with_complex_type():
    """Test when the return type has a complex structure."""
    docstring = parse(
        """
        Returns:
            Optional[Mapping[str, List[int]]]: A description: with a colon
        """
    )
    assert docstring.returns is not None, "Expected returns to be present"
    assert docstring.returns.type_name == "Optional[Mapping[str, List[int]]]", f"Expected type_name to be 'Optional[Mapping[str, List[int]]]' but got {docstring.returns.type_name}"
    assert docstring.returns.description == "A description: with a colon", f"Expected description to be 'A description: with a colon' but got '{docstring.returns.description}'"

def test_parse_empty_return():
    """Test when there is an empty return statement in the docstring."""
    docstring = parse(
        """
        Short description
        Returns:
        """
    )
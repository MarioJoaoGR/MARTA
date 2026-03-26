
import pytest
from docstring_parser.tests.test_rest import parse

def test_returns() -> None:
    """Test parsing returns."""
    # Test case 1: No return value specified
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test case 2: Return description provided
    docstring = parse(
        """
        Short description
        :returns: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator
    assert docstring.many_returns == [docstring.returns]

    # Test case 3: Type specified without description
    docstring = parse(
        """
        Short description
        :returns int:
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == ""  # Default description for type only
    assert not docstring.returns.is_generator
    assert docstring.many_returns == [docstring.returns]

    # Test case 4: Both type and description specified
    docstring = parse(
        """
        Short description
        :returns: description
        :rtype: int
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator
    assert docstring.many_returns == [docstring.returns]

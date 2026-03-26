
from docstring_parser.tests.test_rest import parse

def test_yields() -> None:
    """Test parsing yields."""
    # Test case for no yield declaration
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert len(docstring.many_returns) == 0

    # Test case for yield with description only
    docstring = parse(
        """
        Short description
        :yields: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test case for yield with specific type and description
    docstring = parse(
        """
        Short description
        :yields int: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

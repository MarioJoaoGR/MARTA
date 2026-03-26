
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_returns() -> None:
    """Test parsing returns from a numpy-style docstring."""
    # Test when the docstring is empty
    docstring = parse('')
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test when there is a single return type without description
    docstring = parse("""Returns
                        -------
                        int
                        """)
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test when there is a single return type with description
    docstring = parse("""Returns
                        -------
                        int
                            description
                        """)
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test when there are multiple return types listed in one block
    docstring = parse("""Returns
                        -------
                        int
                            description for a
                        str
                            description for b
                        """)
    assert len(docstring.many_returns) == 2
    assert docstring.many_returns[0].type_name == "int"
    assert docstring.many_returns[0].description == "description for a"
    assert docstring.many_returns[1].type_name == "str"
    assert docstring.many_returns[1].description == "description for b"

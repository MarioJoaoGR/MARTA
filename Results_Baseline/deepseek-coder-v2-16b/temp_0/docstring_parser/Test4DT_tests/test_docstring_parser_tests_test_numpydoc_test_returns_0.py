# Module: docstring_parser.tests.test_numpydoc
# test_numpydoc.py
from docstring_parser import parse
import pytest

def test_no_returns():
    """Test case to check when there is no return specified."""
    docstring = parse("""
    Short description
    """)
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

def test_single_return():
    """Test case to check when there is a single return type without description."""
    docstring = parse("""
    Short description
    Returns
    -------
    int
    """)
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

def test_single_return_with_description():
    """Test case to check when there is a single return type with description."""
    docstring = parse("""
    Short description
    Returns
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

def test_multiple_returns():
    """Test case to check when there are multiple return types with individual descriptions."""
    docstring = parse("""
    Short description
    Returns
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

def test_custom_return_type():
    """Test case to check when there is a custom return type with detailed description including colon."""
    docstring = parse("""
    Short description
    Returns
    -------
    Optional[Mapping[str, List[int]]]
        A description: with a colon
    """)
    assert docstring.returns is not None
    assert docstring.returns.type_name == "Optional[Mapping[str, List[int]]]"
    assert docstring.returns.description == "A description: with a colon"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

def test_multiple_returns_with_descriptions():
    """Test case to check when there are multiple return types with detailed descriptions."""
    docstring = parse("""
    Short description
    Returns
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

if __name__ == "__main__":
    pytest.main()

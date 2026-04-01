
import pytest
from docstring_parser import parse

def test_returns() -> None:
    """Test parsing returns."""
    # Test case 1: No returns specified
    docstring = parse("""Short description""")
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test case 2: Single return type without description
    parsed_docstring = parse("""
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

    # Test case 3: Single return type with a description
    parsed_docstring = parse("""
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

    # Test case 4: Multiple return types with individual descriptions
    parsed_docstring = parse("""
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

    # Test case 5: Custom return type with detailed description including colon
    parsed_docstring = parse("""
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

    # Test case 6: Multiple return types including nested structures
    parsed_docstring = parse("""
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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_returns_2_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_returns_2_test_invalid_inputs.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""
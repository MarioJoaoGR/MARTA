
import pytest
from docstring_parser import parse

def test_returns() -> None:
    """Test parsing returns."""
    docstring = parse(None)
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    docstring = parse("""
        Short description
        Returns
        -------
        type
    """)
    assert docstring.returns is not None
    assert docstring.returns.type_name == "type"
    assert docstring.returns.description is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

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

    docstring = parse("""
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

    docstring = parse("""
        Short description
        Returns
        -------
        int
            description
            with much text

            even some spacing
    """)
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == (
        "description\nwith much text\n\neven some spacing"
    )
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    docstring = parse("""
        Short description
        Returns
        -------
        a : int
            description for a
        b : str
            description for b
    """)
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == ("description for a")
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 2
    assert docstring.many_returns[0].type_name == "int"
    assert docstring.many_returns[0].description == "description for a"
    assert docstring.many_returns[0].return_name == "a"
    assert docstring.many_returns[1].type_name == "str"
    assert docstring.many_returns[1].description == "description for b"
    assert docstring.many_returns[1].return_name == "b"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_returns_5_test_edge_case_2
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_returns_5_test_edge_case_2.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""
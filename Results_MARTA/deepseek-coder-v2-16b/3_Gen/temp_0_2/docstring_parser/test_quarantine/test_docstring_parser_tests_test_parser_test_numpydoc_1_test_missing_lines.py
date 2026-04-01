
import pytest
from docstring_parser.tests.test_parser import parse
from docstring_parser import DocstringStyle

def test_numpydoc() -> None:
    """Test numpydoc-style parser autodetection."""
    docstring = parse(
        """Short description

        Long description

        Causing people to indent:

            A lot sometimes

        Parameters
        ----------
        spam
            spam desc
        bla : int
            bla desc
        yay : str

        Raises
        ------
        ValueError
            exc desc

        Other Parameters
        ----------------
        this_guy : int, optional
            you know him

        Returns
        -------
        tuple
            ret desc

        See Also
        --------
        multiple lines...
        something else?

        Warnings
        --------
        multiple lines...
        none of this is real!
        """
    )

    assert docstring.style == DocstringStyle.NUMPYDOC
    assert docstring.short_description == "Short description"
    assert docstring.long_description == (
        "Long description\n\n"
        "Causing people to indent:\n\n"
        "    A lot sometimes"
    )
    assert docstring.description == (
        "Short description\n\n"
        "Long description\n\n"
        "Causing people to indent:\n\n"
        "    A lot sometimes"
    )
    assert len(docstring.params) == 4
    assert docstring.params[0].arg_name == "spam"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "spam desc"
    assert docstring.params[1].arg_name == "bla"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "bla desc"
    assert docstring.params[2].arg_name == "yay"
    assert docstring.params[2].type_name == "str"
    assert docstring.params[2].description is None
    assert docstring.params[3].arg_name == "this_guy"
    assert docstring.params[3].type_name == "int"
    assert docstring.params[3].is_optional
    assert docstring.params[3].description == "you know him"

    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "exc desc"
    assert docstring.returns is not None
    assert docstring.returns.type_name == "tuple"
    assert docstring.returns.description == "ret desc"
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parser_test_numpydoc_1_test_missing_lines
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_numpydoc_1_test_missing_lines.py:4:0: E0611: No name 'DocstringStyle' in module 'docstring_parser' (no-name-in-module)


"""
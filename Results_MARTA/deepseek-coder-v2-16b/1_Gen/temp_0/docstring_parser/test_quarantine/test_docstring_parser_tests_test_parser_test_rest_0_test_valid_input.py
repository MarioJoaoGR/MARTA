
from docstring_parser import parse, DocstringStyle

def test_rest() -> None:
    """Test ReST-style parser autodetection."""
    docstring = parse(
        """
        Short description

        Long description

        Causing people to indent:

            A lot sometimes

        :param spam: spam desc
        :param int bla: bla desc
        :param str yay:
        :raises ValueError: exc desc
        :returns tuple: ret desc
        """
    )

    assert docstring.style == DocstringStyle.REST
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
    assert len(docstring.params) == 3
    assert docstring.params[0].arg_name == "spam"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "spam desc"
    assert docstring.params[1].arg_name == "bla"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "bla desc"
    assert docstring.params[2].arg_name == "yay"
    assert docstring.params[2].type_name == "str"
    assert docstring.params[2].description == ""
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
************* Module Test4DT_tests.test_docstring_parser_tests_test_parser_test_rest_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_rest_0_test_valid_input.py:2:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_rest_0_test_valid_input.py:2:0: E0611: No name 'DocstringStyle' in module 'docstring_parser' (no-name-in-module)

"""
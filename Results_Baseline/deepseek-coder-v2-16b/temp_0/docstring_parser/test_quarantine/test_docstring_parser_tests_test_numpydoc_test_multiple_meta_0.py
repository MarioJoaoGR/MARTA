
# Module: docstring_parser.tests.test_numpydoc
# test_multiple_meta.py
from docstring_parser.tests.test_numpydoc import test_multiple_meta

def test_multiple_meta():
    """Test parsing multiple meta."""
    from docstring_parser import parse  # Importing here to resolve the undefined variable error

    docstring = parse(
        """
        Short description

        Parameters
        ----------
        spam
            asd
            1
                2
            3

        Raises
        ------
        bla
            herp
        yay
            derp
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 3
    assert docstring.meta[0].args == ["param", "spam"]
    assert docstring.meta[0].arg_name == "spam"
    assert docstring.meta[0].description == "asd\n1\n    2\n3"
    assert docstring.meta[1].args == ["raises", "bla"]
    assert docstring.meta[1].type_name == "bla"
    assert docstring.meta[1].description == "herp"
    assert docstring.meta[2].args == ["raises", "yay"]
    assert docstring.meta[2].type_name == "yay"
    assert docstring.meta[2].description == "derp"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_multiple_meta_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_multiple_meta_0.py:6:0: E0102: function already defined line 4 (function-redefined)

"""
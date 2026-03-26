
# Module: docstring_parser.tests.test_numpydoc
# Import the function from its module
from docstring_parser.tests.test_numpydoc import test_meta_with_multiline_description

def test_parse():
    # Test parsing a numpy-style docstring with a short description and a meta entry with a multi-line argument description
    from docstring_parser import parse  # Corrected the import statement to include 'parse'

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
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    meta = docstring.meta[0]
    assert meta.args == ["param", "spam"]
    assert meta.arg_name == "spam"
    assert meta.description == "asd\n1\n    2\n3"

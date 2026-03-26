
# Module: docstring_parser.tests.test_numpydoc
# Import the function using its module name
from docstring_parser.tests.test_numpydoc import test_meta_with_multiline_description

def test_parse():
    # Test case for parsing a multiline docstring with parameters
    from docstring_parser import parse  # Importing the function here to resolve pylint error
    
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
    
    # Assertions to check the parsed results
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["param", "spam"]
    assert docstring.meta[0].arg_name == "spam"
    assert docstring.meta[0].description == "asd\n1\n    2\n3"

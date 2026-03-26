
# Module: docstring_parser.tests.test_numpydoc
# Import the function using its provided module name
from docstring_parser import parse

def test_parse():
    # Test parsing a docstring with multiple meta (parameters and raises)
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
    
    # Assertions for short description
    assert docstring.short_description == "Short description"
    
    # Assertions for metadata count and structure
    assert len(docstring.meta) == 3
    
    # First meta (parameter) assertions
    assert docstring.meta[0].args == ["param", "spam"]
    assert docstring.meta[0].arg_name == "spam"
    assert docstring.meta[0].description == "asd\n1\n    2\n3"
    
    # Second meta (raises) assertions
    assert docstring.meta[1].args == ["raises", "bla"]
    assert docstring.meta[1].type_name == "bla"
    assert docstring.meta[1].description == "herp"
    
    # Third meta (raises) assertions
    assert docstring.meta[2].args == ["raises", "yay"]
    assert docstring.meta[2].type_name == "yay"
    assert docstring.meta[2].description == "derp"


# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse

def test_multiple_meta():
    """Test parsing multiple meta."""
    # Test case for the function with a multi-line description and metadata entries
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
    
    # Assertions for short description and metadata entries
    assert docstring.short_description == "Short description"
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

# Additional test case to cover line 322 directly
def test_parse_functionality():
    """Test the functionality of the parse function with multiple meta."""
    # Test case for parsing a docstring with multiple metadata entries
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
    
    # Assertions for short description and metadata entries
    assert docstring.short_description == "Short description"
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

# Additional test case to cover uncovered lines 342-352 directly
def test_parse_multiple_meta():
    """Test the parse function with multiple meta entries."""
    # Test case for parsing a docstring with multiple metadata entries
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
    
    # Assertions for short description and metadata entries
    assert docstring.short_description == "Short description"
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

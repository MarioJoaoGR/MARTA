
from docstring_parser import parse

def test_meta_with_multiline_description():
    """Test parsing multiline meta documentation."""
    docstring = parse(
        """
        Short description

        Args:
            spam: asd
                1
                    2
                3
        """
    )
    
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["param", "spam"]
    assert docstring.meta[0].arg_name == "spam"
    assert docstring.meta[0].description == "asd\n1\n    2\n3"

def test_meta_with_empty_docstring():
    """Test parsing an empty docstring."""
    # Test case 2: Empty docstring
    docstring = parse("")
    
    assert docstring.short_description is None
    assert len(docstring.meta) == 0

def test_meta_with_no_meta_section():
    """Test parsing a docstring without a meta section."""
    # Test case 3: Docstring without a meta section
    docstring = parse(
        """
        Short description
        """
    )
    
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 0

def test_meta_with_multiple_meta():
    """Test parsing a docstring with multiple meta sections."""
    # Test case 4: Docstring with multiple meta sections
    docstring = parse(
        """
        Short description

        Args:
            spam: asd
                1
                    2
                3

        Returns:
            eggs: qwe
                4
                        5
                    6
        """
    )
    
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args == ["param", "spam"]
    assert docstring.meta[0].arg_name == "spam"
    assert docstring.meta[0].description == "asd\n1\n    2\n3"
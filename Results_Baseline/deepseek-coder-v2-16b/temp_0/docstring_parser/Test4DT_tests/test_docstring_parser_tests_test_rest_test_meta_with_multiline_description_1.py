
# Module: docstring_parser.tests.test_rest
from docstring_parser import parse

def test_meta_with_multiline_description() -> None:
    """Test parsing multiline meta documentation."""
    # Existing test case for reference
    docstring = parse(
        """
        Short description

        :meta: asd
            1
                2
            3
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["meta"]
    assert docstring.meta[0].description == "asd\n1\n    2\n3"

# Additional test case to cover line 211 and ensure correct parsing of the meta entry
def test_parse_multiline_meta_docstring() -> None:
    """Test parsing a docstring with a multiline meta description."""
    # Arrange
    docstring = parse(
        """
        Short description

        :meta: example argument
            1
                2
            3
        """
    )
    
    # Act and Assert
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["meta"]
    assert docstring.meta[0].description == "example argument\n1\n    2\n3"

# Additional test case to cover lines 221-224 and ensure correct parsing of the meta entry
def test_parse_multiline_meta_docstring_with_different_content() -> None:
    """Test parsing a docstring with a multiline meta description containing different content."""
    # Arrange
    docstring = parse(
        """
        Short description

        :meta: another example
            1
                2
            3
        """
    )
    
    # Act and Assert
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["meta"]
    assert docstring.meta[0].description == "another example\n1\n    2\n3"

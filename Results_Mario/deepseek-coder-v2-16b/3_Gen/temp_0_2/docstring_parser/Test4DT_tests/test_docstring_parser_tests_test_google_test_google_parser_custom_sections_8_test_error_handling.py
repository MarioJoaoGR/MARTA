
from docstring_parser.tests.test_google import GoogleParser, Section, SectionType

def test_google_parser_custom_sections() -> None:
    """Test parsing an unknown section with custom GoogleParser configuration.
    
    This function initializes a `GoogleParser` object with a predefined list of sections, including DESCRIPTION, ARGUMENTS, ATTRIBUTES, and EXAMPLES. It then parses a sample docstring that includes these sections to verify the parser's ability to extract information from custom sections. The test checks if the parsed meta data contains the expected section titles and descriptions.
    
    Parameters:
        None.
        
    Returns:
        None.
        
    Examples:
        >>> test_google_parser_custom_sections()
        This function does not return any value but will raise assertions if the parsing of the custom sections fails or the expected meta data is incorrect.
    
    Intended to do:
        Test the parsing of a custom GoogleParser configuration for an unknown section, including multiple and singular sections like ARGUMENTS, ATTRIBUTES, and EXAMPLES.
        
        This function sets up a specific configuration for the GoogleParser to parse a docstring with custom sections and verifies that the parsed information matches expectations. It checks for the presence of short and long descriptions, as well as the detailed meta data from each section.
        
        Args:
            None
            
        Returns:
            None
    """
    parser = GoogleParser(
        [
            Section("DESCRIPTION", "desc", SectionType.SINGULAR),
            Section("ARGUMENTS", "param", SectionType.MULTIPLE),
            Section("ATTRIBUTES", "attribute", SectionType.MULTIPLE),
            Section("EXAMPLES", "examples", SectionType.SINGULAR),
        ],
        title_colon=False,
    )
    docstring = parser.parse(
        """
        DESCRIPTION
            This is the description.

        ARGUMENTS
            arg1: first arg
            arg2: second arg

        ATTRIBUTES
            attr1: first attribute
            attr2: second attribute

        EXAMPLES
            Many examples
            More examples
        """
    )

    assert docstring.short_description is None
    assert docstring.long_description is None
    assert len(docstring.meta) == 6
    assert docstring.meta[0].args == ["desc"]
    assert docstring.meta[0].description == "This is the description."
    assert docstring.meta[1].args == ["param", "arg1"]
    assert docstring.meta[1].description == "first arg"
    assert docstring.meta[2].args == ["param", "arg2"]
    assert docstring.meta[2].description == "second arg"
    assert docstring.meta[3].args == ["attribute", "attr1"]
    assert docstring.meta[3].description == "first attribute"
    assert docstring.meta[4].args == ["attribute", "attr2"]
    assert docstring.meta[4].description == "second attribute"
    assert docstring.meta[5].args == ["examples"]
    assert docstring.meta[5].description == "Many examples\nMore examples"


import pytest
from docstring_parser.google import GoogleParser, Section, SectionType

def test_google_parser_custom_sections() -> None:
    """Test parsing an unknown section with custom GoogleParser configuration.
    
    This function initializes a GoogleParser object with a predefined list of sections including DESCRIPTION, ARGUMENTS, ATTRIBUTES, and EXAMPLES. It then parses a sample docstring that includes these sections to verify the parser's ability to handle custom sections. The test checks if the parsed meta information correctly captures the descriptions provided in each section.
    
    Parameters:
        None
        
    Returns:
        None
        
    Examples:
        >>> test_google_parser_custom_sections()
        This function does not take any parameters, but it demonstrates how to configure and use a GoogleParser with custom sections for parsing docstrings. The expected outcome is that the parser correctly identifies and extracts descriptions from each section in the provided sample docstring.
        
    Intended Usage:
        The function is designed to test the parsing capabilities of a custom GoogleParser configuration for an unknown section, ensuring it can handle multiple and singular sections like ARGUMENTS, ATTRIBUTES, and EXAMPLES without using title colon formatting. It verifies that the parser correctly extracts information from these sections and handles them appropriately.
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

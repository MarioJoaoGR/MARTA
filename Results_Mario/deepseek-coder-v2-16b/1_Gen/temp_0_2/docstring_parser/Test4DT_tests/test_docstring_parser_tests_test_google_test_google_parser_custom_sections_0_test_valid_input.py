
import pytest
from docstring_parser.tests.test_google import GoogleParser, Section, SectionType

def test_google_parser_custom_sections() -> None:
    """Test parsing an unknown section with custom GoogleParser configuration.
    
    This function sets up a `GoogleParser` instance with specific sections for 'DESCRIPTION', 'ARGUMENTS', 'ATTRIBUTES', and 'EXAMPLES'. It configures the parser to not include colons after section titles. The function then parses a sample docstring containing these sections and asserts that the parsed meta information matches expected values, including short and long descriptions being None and six meta items with specific arguments and descriptions.
    
    Parameters:
        - (None): This function does not take any parameters as input.
        
    Returns:
        - (None): The function does not return anything but performs assertions on the parsed docstring to ensure correctness.
        
    Example:
        # Running the test function will set up and parse a custom GoogleParser configuration with specified sections, then assert expected outcomes based on the parsed content of the sample docstring.
    
    Intended Purpose:
    Test the parsing of a custom GoogleParser configuration for an unknown section, including handling multiple and singular sections such as ARGUMENTS, ATTRIBUTES, and EXAMPLES.
    
    This function sets up a specific configuration for the GoogleParser to parse a docstring with custom sections and verifies that the parsed information matches the expected results. It checks for the presence of short and long descriptions, as well as the detailed meta information extracted from each section.
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

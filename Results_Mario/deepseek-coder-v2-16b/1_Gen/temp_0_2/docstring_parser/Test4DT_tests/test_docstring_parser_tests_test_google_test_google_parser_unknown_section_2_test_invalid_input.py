
from docstring_parser.tests.test_google import GoogleParser

def test_google_parser_unknown_section() -> None:
    """Test parsing an unknown section with default GoogleParser configuration.
    
    This function is designed to verify the functionality of the `GoogleParser` when it encounters a section in a docstring that is not predefined within its configuration settings. It sets up a parser instance with standard configurations, which are configured to recognize only the default sections. The function then attempts to parse a sample docstring containing an "Unknown" section. After parsing, it asserts that:
    1. The short description of the parsed result should be "Unknown:".
    2. The long description should include the content "spam: a".
    3. There are no meta-data entries in the parsed output.
    
    Examples:
        # Running the test case directly, which will assert based on expected outcomes.
        test_google_parser_unknown_section()
        
        This example demonstrates how to run the function without making any changes or assertions, as it is a direct test of the `GoogleParser` parsing capabilities for an unknown section under default settings.
    """
    parser = GoogleParser()
    docstring = parser.parse(
        """
        Unknown:
            spam: a
        """
    )
    assert docstring.short_description == "Unknown:"
    assert docstring.long_description == "spam: a"
    assert len(docstring.meta) == 0

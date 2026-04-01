
import pytest
from docstring_parser.tests.test_google import GoogleParser

def test_google_parser_multi_line_parameter_type() -> None:
    """Test parsing a multi-line parameter type with default GoogleParser."""
    parser = GoogleParser()
    docstring = parser.parse(
        """Description of the function.

        Args:
            output_type (Literal["searchResults", "sourcedAnswer", "structured"]): The type of output expected from the parsed docstring. This parameter is used to specify what kind of information should be extracted or represented in the final output, such as search results, sourced answers, or structured data formats.

        Returns:
            bool: Indicates whether the parsing operation was successful or not. A return value of True indicates that the function parsed the docstring correctly and handled the multi-line parameter type as expected.

        Examples:
            # Example usage to test default GoogleParser behavior with a multi-line argument description in a docstring
            test_google_parser_multi_line_parameter_type()
            
            This example demonstrates how to call the function without any customizations, ensuring that it operates under the default conditions and verifies its ability to handle multiple lines of text within an argument's description.
        """
    )
    assert docstring.params[0].arg_name == "output_type"

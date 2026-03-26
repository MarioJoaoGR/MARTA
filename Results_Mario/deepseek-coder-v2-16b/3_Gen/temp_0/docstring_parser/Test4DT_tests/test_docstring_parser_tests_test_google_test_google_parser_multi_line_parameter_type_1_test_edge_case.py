
import pytest
from docstring_parser.tests.test_google import GoogleParser

def test_google_parser_multi_line_parameter_type():
    """Test parsing a multi-line parameter type with default GoogleParser"""
    parser = GoogleParser()
    docstring = parser.parse(
        """Description of the function.

        Args:
            output_type (Literal["searchResults", "sourcedAnswer",
                "structured"]): The type of output.
                This can be one of the following:
                - "searchResults": Represents the search results.
                - "sourcedAnswer": Represents a sourced answer.
                - "structured": Represents a structured output format.

        Returns:
            bool: Indicates success or failure.

        """
    )
    assert docstring.params[0].arg_name == "output_type"

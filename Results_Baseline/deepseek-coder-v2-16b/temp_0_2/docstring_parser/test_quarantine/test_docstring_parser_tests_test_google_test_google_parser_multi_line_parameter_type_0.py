
# Module: docstring_parser.tests.test_google
from docstring_parser import GoogleParser  # Corrected import statement

def test_google_parser_multi_line_parameter_type():
    """Test parsing a multi-line parameter type with default GoogleParser"""
    parser = GoogleParser()  # Instantiate the parser correctly
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
    assert docstring.params[0].arg_name == "output_type"  # Corrected assertion

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_google_parser_multi_line_parameter_type_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_google_parser_multi_line_parameter_type_0.py:3:0: E0611: No name 'GoogleParser' in module 'docstring_parser' (no-name-in-module)

"""
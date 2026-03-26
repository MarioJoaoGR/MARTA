
# Module: docstring_parser.tests.test_google
# Import the function using its provided module name
from docstring_parser.tests.test_google import parse

def test_parse():
    # Test parsing a docstring with a short description and a multiline argument description
    parsed_docstring = parse(
        """
        Short description

        Args:
            spam: asd
                1
                    2
                3
        """
    )
    
    # Assertions to verify the parsing results
    assert parsed_docstring.short_description == "Short description"
    assert len(parsed_docstring.meta) == 1
    assert parsed_docstring.meta[0].args == ["param", "spam"]
    assert parsed_docstring.meta[0].arg_name == "spam"
    assert parsed_docstring.meta[0].description == "asd\n1\n    2\n3"

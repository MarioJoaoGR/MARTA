
from docstring_parser.tests.test_epydoc import parse, compose

def test_short_rtype() -> None:
    """Test function to verify the parsing of a short docstring containing only return type information.

    This function constructs and parses a test docstring with a brief description followed by an RTYP (return type) directive, then asserts that the parsed result matches the original string. It is designed for testing the functionality of the `parse` function in handling abbreviated docstrings.

    Parameters:
        None

    Returns:
        None

    Notes:
        - This test is designed to check the parsing and recomposition of a minimal docstring containing only a description and an RTYP annotation.
        - The `parse` function is used to convert the string representation of the docstring into a structured format, while the `compose` function is then used to render this parsed structure back into a string.
        - The test asserts that the result of parsing and recomposing the docstring matches the original input, ensuring data integrity during conversion processes.
    """
    string = "Short description.\n\n@rtype: float"
    docstring = parse(string)
    assert compose(docstring) == string

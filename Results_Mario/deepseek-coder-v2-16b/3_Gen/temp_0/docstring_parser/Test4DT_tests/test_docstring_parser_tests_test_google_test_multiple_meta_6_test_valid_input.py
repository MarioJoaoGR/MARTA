
import pytest
from docstring_parser.tests.test_google import parse  # Assuming this is where parse function is defined or mocked

def test_multiple_meta() -> None:
    """Test parsing multiple meta in a Google-style docstring.

    This function tests the parsing of a Google-style docstring by creating a sample docstring, parsing it using the `parse` function, and then asserting that the parsed components match expected values. The test checks for the presence of the short description, the number of metadata entries, and the details of each metadata entry (including argument name, type, and description).

    Parameters:
        None

    Returns:
        None

    Examples:
        ```python
        from docstring_parser.tests.test_google import parse  # Assuming this is where parse function is defined or mocked

        # Run the test function to ensure it works as expected
        test_multiple_meta()
        
        # If all assertions pass, this indicates that the docstring parsing is functioning correctly.
        ```
    """
    docstring = parse(
        """
        Short description

        Args:
            spam: asd
                1
                    2
                3

        Raises:
            bla: herp
            yay: derp
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 3
    assert docstring.meta[0].args == ["param", "spam"]
    assert docstring.meta[0].arg_name == "spam"
    assert docstring.meta[0].description == "asd\n1\n    2\n3"
    assert docstring.meta[1].args == ["raises", "bla"]
    assert docstring.meta[1].type_name == "bla"
    assert docstring.meta[1].description == "herp"
    assert docstring.meta[2].args == ["raises", "yay"]
    assert docstring.meta[2].type_name == "yay"
    assert docstring.meta[2].description == "derp"

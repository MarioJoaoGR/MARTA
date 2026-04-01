
import pytest
from docstring_parser.tests.test_google import parse

def test_unknown_meta() -> None:
    """Test parsing unknown meta in a Google-style docstring.

    This function tests the ability to parse and handle sections of a Google-style docstring that are not predefined, such as "Unknown0", "Unknown1", etc. It constructs a sample docstring with these unknown sections and then asserts that the parameters within these sections are correctly parsed based on their descriptions.

    Args:
        None

    Returns:
        None

    Examples:
        >>> from google_parser import parse, test_unknown_meta
        >>> # Assuming you have a Google-style docstring parser implemented as 'parse' function
        >>> test_unknown_meta()  # This will run the test and assert that unknown sections are parsed correctly

    Notes:
        - The function does not take any parameters.
        - It constructs a sample docstring with predefined and unknown sections to ensure that the parser can handle unexpected section titles.
        - After parsing, it asserts that the arguments within these unknown sections have their correct names and descriptions as specified in the example docstring.
    """
    docstring = parse(
        """Short desc

        Unknown 0:
            title0: content0

        Args:
            arg0: desc0
            arg1: desc1

        Unknown1:
            title1: content1

        Unknown2:
            title2: content2
        """
    )

    assert docstring.params[0].arg_name == "arg0"
    assert docstring.params[0].description == "desc0"
    assert docstring.params[1].arg_name == "arg1"
    assert docstring.params[1].description == "desc1"

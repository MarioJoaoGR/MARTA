
import pytest
from docstring_parser.tests.test_parser import parse, DocstringStyle, ParseError

def test_autodetection_error_detection() -> None:
    """Test autodection for the case where one of the parsers throws an error and another one succeeds.

    This function simulates a scenario where a docstring is parsed with two different styles, one of which should raise a `ParseError`. It asserts that the parsing process correctly identifies the failure by raising the expected exception when using the incorrect style. Additionally, it verifies that autodetection still works and parses the docstring into its components based on the default or automatically detected style.

    Parameters:
        None

    Returns:
        None

    Examples:
        This function does not take any parameters and is designed to be run directly as a test case in a testing framework, asserting that errors are handled correctly when parsing with incorrect styles.
    
    Intended Usage:
        The intended purpose of this function is to test the automatic detection mechanism of the `parse` function when it encounters a malformed docstring, and ensure that the error handling works correctly by raising a `ParseError`. It also checks if autodetection still functions properly even after encountering an invalid docstring format.
    """
    source = """
    Does something useless

    :param 3 + 3 a: a param
    """

    with pytest.raises(ParseError):
        # assert that one of the parsers does raise
        parse(source, DocstringStyle.REST)

    # assert that autodetection still works
    docstring = parse(source)

    assert docstring
    assert docstring.style == DocstringStyle.GOOGLE

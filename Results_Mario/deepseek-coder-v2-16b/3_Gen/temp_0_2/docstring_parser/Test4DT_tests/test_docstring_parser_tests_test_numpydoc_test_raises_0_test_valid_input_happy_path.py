
from docstring_parser.tests.test_numpydoc import parse

def test_raises() -> None:
    """Test parsing raises.

    This function tests the ability of the `parse` function to correctly parse and identify raised exceptions in a docstring. It does so by attempting to parse two different types of docstrings: one without any exception declarations and one with an explicit "Raises" section. The function then asserts that the number of raised exceptions and their details match what is expected based on the content of the docstring.

    Parameters:
        None

    Returns:
        A parsed object containing information about the raised exceptions, including their type names and descriptions. If no exceptions are mentioned in the docstring, it returns an empty list.

    Usage:
        The function can be called directly with a string representing a Python docstring. It will parse the docstring and return an object encapsulating the parsed data. Example usage includes integrating this parser into automated documentation generation tools or applications that require detailed information about exceptions from docstrings.

    Significance:
        This function is crucial for ensuring the accuracy of exception handling in code by allowing developers to programmatically check if a specific error condition is documented correctly. It supports various docstring styles and provides a way to automate the extraction of exception details, which can be used for documentation generation, runtime validation, or other automated processes that require understanding the expected errors within functions or classes defined through docstrings.
    """
    # Test with no raises section in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0

    # Test with a raises section in the docstring
    docstring = parse(
        """
        Short description
        Raises
        ------
        ValueError
            description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"

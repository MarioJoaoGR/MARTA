
import pytest
from docstring_parser.tests.test_rest import parse

def test_meta_with_args() -> None:
    """Test parsing meta with additional arguments.

    This function simulates the process of parsing a ReST-style docstring that includes metadata with specific arguments. It checks whether the parsed docstring correctly captures the provided metadata and verifies its presence in the `meta` list of the `Docstring` object. The test involves creating a sample docstring with a single meta entry containing specific arguments and ensuring that this meta entry is accurately parsed by the `parse` function.

    Examples:
        >>> test_meta_with_args()
        This will run the test, parsing the provided docstring and asserting that it correctly captures the metadata specified in the example. The exact output depends on how the `parse` function is implemented but should include assertions about the presence of meta data with specific arguments.

    Parameters:
        None

    Returns:
        None
    """
    docstring = parse(
        """
        Short description

        :meta ene due rabe: asd
        """
    )
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["meta", "ene", "due", "rabe"]
    assert docstring.meta[0].description == "asd"

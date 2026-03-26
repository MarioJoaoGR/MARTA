
from docstring_parser.tests.test_google import parse

def test_examples():
    """Test parsing examples."""
    docstring = parse(
        """
        Short description
        Example:
            example: 1
        Examples:
            long example

            more here
        """
    )
    assert len(docstring.examples) == 2
    assert docstring.examples[0].description == "example: 1"
    assert docstring.examples[1].description == "long example\n\nmore here"

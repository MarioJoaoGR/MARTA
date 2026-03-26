
# Module: docstring_parser.tests.test_epydoc
from docstring_parser import parse

def test_returns() -> None:
    """Test parsing returns from an epydoc-style docstring."""
    
    # Test case 4: Return type specified with a description and is_generator set to True
    docstring = parse(
        """
        Short description
        @return: description
        @is_generator: True
        """
    )
    assert docstring.returns is not None
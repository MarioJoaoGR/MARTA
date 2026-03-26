
from docstring_parser.tests.test_numpydoc import parse

def test_invalid_inputs() -> None:
    """Test parsing returns from a numpy-style docstring with invalid inputs."""
    # Test case for no return section in the docstring
    docstring = parse(
        """
        Short description without any returns section.
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test case for invalid return type in the docstring
    docstring = parse(
        """
        Short description
        Returns
        -------
        InvalidType
            Description with a typo.
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "InvalidType"
    assert docstring.returns.description == "Description with a typo."
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns


from docstring_parser import parse

def test_multiple_meta() -> None:
    """Test parsing multiple meta."""
    # Test case for parsing a docstring with multiple meta (parameters and raises)
    docstring = parse(
        """
        Short description

        Parameters
        ----------
        spam
            asd
            1
                2
            3

        Raises
        ------
        bla
            herp
        yay
            derp
        """
    )
    
    # Assertions for short description
    assert docstring.short_description == "Short description"
    
    # Assertions for metadata count and structure
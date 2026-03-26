
# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse

def test_parse():
    """Test parsing a simple docstring with all sections."""
    docstring = parse(
        """
        Short description

        See Also
        --------
        something : some thing you can also see
        actually, anything can go in this section

        Warnings
        --------
        Here be dragons

        Notes
        -----
        None of this is real

        References
        ----------
        Cite the relevant literature, e.g. [1]_.  You may also cite these
        references in the notes section above.

        .. [1] O. McNoleg, "The integration of GIS, remote sensing,
           expert systems and adaptive co-kriging for environmental habitat
           modelling of the Highland Haggis using object-oriented, fuzzy-logic
           and neural-network techniques," Computers & Geosciences, vol. 22,
           pp. 585-588, 1996.
        """
    )
    
    # Check if there are exactly four meta components
    assert len(docstring.meta) == 4
    
    # Check the content of each section
    see_also = docstring.meta[0]
    warnings = docstring.meta[1]
    notes = docstring.meta[2]
    references = docstring.meta[3]
    
    assert see_also.args == ["see_also"]
    assert see_also.description == (
        "something : some thing you can also see\n"
        "actually, anything can go in this section"
    )
    
    assert warnings.args == ["warnings"]
    assert warnings.description == "Here be dragons"
    
    assert notes.args == ["notes"]
    assert notes.description == "None of this is real"

def test_parse_no_sections():
    """Test parsing a docstring with no sections."""
    docstring = parse("Short description")
    assert len(docstring.meta) == 0

def test_parse_missing_section():
    """Test parsing a docstring missing some sections."""
    docstring = parse(
        """
        Short description

        See Also
        --------
        something : some thing you can also see

        Notes
        -----
        None of this is real
        """
    )
    assert len(docstring.meta) == 2

def test_parse_extra_section():
    """Test parsing a docstring with an extra section."""
    docstring = parse(
        """
        Short description

        See Also
        --------
        something : some thing you can also see

        Warnings
        --------
        Here be dragons

        Notes
        -----
        None of this is real

        Extra Section
        --------------
        Just a test section
        """
    )
    assert len(docstring.meta) == 3

def test_parse_invalid_section():
    """Test parsing a docstring with an invalid section."""
    docstring = parse(
        """
        Short description

        Invalid Section
        ----------------
        Just some text

        See Also
        --------
        something : some thing you can also see

        Warnings
        --------
        Here be dragons

        Notes
        -----
        None of this is real
        """
    )
    assert len(docstring.meta) == 3

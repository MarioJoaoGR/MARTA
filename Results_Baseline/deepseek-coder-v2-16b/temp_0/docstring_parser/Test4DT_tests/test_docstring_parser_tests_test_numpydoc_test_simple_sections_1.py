
# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse

def test_simple_sections():
    """Test parsing simple sections."""
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
    
    # Additional test cases to cover uncovered lines
    assert len(docstring.meta) == 4
    
    # Test case for the first meta object in docstring.meta
    assert docstring.meta[0].args == ["see_also"]
    assert docstring.meta[0].description == (
        "something : some thing you can also see\n"
        "actually, anything can go in this section"
    )
    
    # Test case for the second meta object in docstring.meta
    assert docstring.meta[1].args == ["warnings"]
    assert docstring.meta[1].description == "Here be dragons"
    
    # Test case for the third meta object in docstring.meta
    assert docstring.meta[2].args == ["notes"]
    assert docstring.meta[2].description == "None of this is real"
    
    # Test case for the fourth meta object in docstring.meta
    assert docstring.meta[3].args == ["references"]

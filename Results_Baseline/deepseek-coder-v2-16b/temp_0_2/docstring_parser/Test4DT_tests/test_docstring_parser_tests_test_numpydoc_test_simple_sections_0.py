
# Module: docstring_parser.tests.test_numpydoc
# Import the function using its module name
from docstring_parser import parse

def test_parse():
    # Test parsing a simple docstring with all sections
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
    
    assert references.args == ["references"]
    # Add more specific assertions for the reference content if needed

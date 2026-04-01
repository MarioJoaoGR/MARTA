
import pytest
from docstring_parser import parse

def test_simple_sections():
    """Test parsing simple sections of a numpy-style docstring."""
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
    assert len(docstring.meta) == 4
    assert docstring.meta[0].args == ["see_also"]
    assert docstring.meta[0].description == (
        "something : some thing you can also see\n"
        "actually, anything can go in this section"
    )

    assert docstring.meta[1].args == ["warnings"]
    assert docstring.meta[1].description == "Here be dragons"

    assert docstring.meta[2].args == ["notes"]
    assert docstring.meta[2].description == "None of this is real"

    assert docstring.meta[3].args == ["references"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_simple_sections_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_simple_sections_0_test_valid_input.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""
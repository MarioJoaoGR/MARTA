
from docstring_parser.tests.test_numpydoc import parse

def test_simple_sections() -> None:
    """Test parsing simple sections of a numpy-style docstring.

    This function tests the ability to parse various sections from a numpy-style docstring, including "See Also", "Warnings", "Notes", and "References". It verifies that each section is correctly identified and parsed into its respective metadata object within the `Docstring` object returned by the `parse` function. The function checks that there are exactly four meta objects in the `docstring.meta` list, corresponding to the four sections: "See Also", "Warnings", "Notes", and "References". It also verifies the content of each meta object's arguments and descriptions.

    Examples:
        To run this test function and ensure it works correctly, you can call it directly in your Python script or environment where it is defined:
        
        ```python
        from docstring_parser.tests.test_numpydoc import parse

        # Run the test function
        test_simple_sections()
        ```

    This function does not take any parameters. It relies on the `parse` function to parse a sample numpy-style docstring and then asserts that the parsed result contains exactly four meta objects, each with their respective arguments and descriptions as expected for "See Also", "Warnings", "Notes", and "References" sections in a numpy-style docstring.
    """
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

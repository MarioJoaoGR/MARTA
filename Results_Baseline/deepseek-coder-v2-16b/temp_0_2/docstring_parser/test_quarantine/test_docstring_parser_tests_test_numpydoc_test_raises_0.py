
# Module: docstring_parser.tests.test_numpydoc
# test_numpydoc.py
from your_module import parse, Docstring

def test_raises():
    """Test parsing raises."""
    
    # Test case 1: No 'Raises' section in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0, "Expected no raises but found some."

    # Test case 2: With a single 'Raises' entry in the docstring
    docstring = parse(
        """
        Short description
        Raises
        ------
        ValueError
            description
        """
    )
    assert len(docstring.raises) == 1, "Expected one raise but found more."
    assert docstring.raises[0].type_name == "ValueError", f"Expected type 'ValueError' but got {docstring.raises[0].type_name}."
    assert docstring.raises[0].description == "description", f"Expected description 'description' but got '{docstring.raises[0].description}'."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_raises_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_raises_0.py:4:0: E0401: Unable to import 'your_module' (import-error)

"""

def test_raises() -> None:
    """Test parsing raises."""
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0

    docstring = parse(
        """
        Short description
        Raises
        ------
        ValueError
            description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_raises_3_test_valid_case_happy_path
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_raises_3_test_valid_case_happy_path.py:4:16: E0602: Undefined variable 'parse' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_raises_3_test_valid_case_happy_path.py:11:16: E0602: Undefined variable 'parse' (undefined-variable)


"""
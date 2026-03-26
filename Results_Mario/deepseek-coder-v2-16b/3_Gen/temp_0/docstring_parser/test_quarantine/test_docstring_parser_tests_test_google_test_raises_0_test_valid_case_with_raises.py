
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
        Raises:
            ValueError: description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_raises_0_test_valid_case_with_raises
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_0_test_valid_case_with_raises.py:4:16: E0602: Undefined variable 'parse' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_0_test_valid_case_with_raises.py:11:16: E0602: Undefined variable 'parse' (undefined-variable)


"""
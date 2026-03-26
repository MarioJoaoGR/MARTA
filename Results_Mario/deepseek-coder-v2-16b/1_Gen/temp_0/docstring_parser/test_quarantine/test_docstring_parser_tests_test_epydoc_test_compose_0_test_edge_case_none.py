
def test_compose(source: str, expected: str) -> None:
    """Test compose in default mode."""
    parsed = parse(source)
    composed = compose(parsed)
    assert composed == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_compose_0_test_edge_case_none
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_edge_case_none.py:4:13: E0602: Undefined variable 'parse' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_edge_case_none.py:5:15: E0602: Undefined variable 'compose' (undefined-variable)

"""
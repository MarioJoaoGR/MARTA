
from docstring_parser import parse
import pytest

def test_meta_with_multiline_description() -> None:
    """Test parsing multiline meta documentation."""
    # Test case where the function should raise an exception due to malformed docstring
    with pytest.raises(Exception):
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
            """
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_meta_with_multiline_description_5_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_meta_with_multiline_description_5_test_invalid_input.py:2:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""
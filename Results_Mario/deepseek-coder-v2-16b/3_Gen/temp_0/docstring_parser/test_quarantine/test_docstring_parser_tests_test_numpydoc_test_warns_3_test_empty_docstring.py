
from docstring_parser.tests.test_numpydoc import parse
import warnings

def test_warns() -> None:
    """Test parsing warns."""
    with warnings.catch_warnings(record=True) as w:
        # Trigger a warning
        warnings.simplefilter("always")
        docstring = parse(
            """
            Short description
            Warns
            -----
            UserWarning
                description
            """
        )
    assert len(docstring.meta) == 1
    assert isinstance(docstring.meta[0], warnings.WarningMessage)
    assert docstring.meta[0].category == warnings.UserWarning
    assert str(docstring.meta[0]) == "description"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_warns_3_test_empty_docstring
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_warns_3_test_empty_docstring.py:21:41: E1101: Module 'warnings' has no 'UserWarning' member (no-member)


"""
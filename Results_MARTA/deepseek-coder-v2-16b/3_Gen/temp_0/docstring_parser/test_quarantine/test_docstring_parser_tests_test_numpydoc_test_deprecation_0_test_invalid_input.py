
import pytest
from docstring_parser import parse
import typing as T

@pytest.mark.parametrize("source, expected_depr_version, expected_depr_desc", [
    ("""
    Some function to demonstrate deprecation.
    
    Deprecated since version 1.0.0: Use another_function instead.
    """, "1.0.0", "Use another_function instead."),
    ("""
    Some function to demonstrate no deprecation.
    """, None, None)
])
def test_deprecation(source, expected_depr_version, expected_depr_desc):
    docstring = parse(source)
    
    if expected_depr_version is not None:
        assert docstring.deprecation is not None
        assert docstring.deprecation.version == expected_depr_version
        assert docstring.deprecation.description == expected_depr_desc
    else:
        with pytest.raises(AttributeError):
            assert docstring.deprecation is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_invalid_input.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""
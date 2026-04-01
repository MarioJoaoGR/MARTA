
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_deprecation(
    source: str,
    expected_depr_version: T.Optional[str],
    expected_depr_desc: T.Optional[str],
) -> None:
    """Test parsing deprecation notes."""
    docstring = parse(source)

    assert docstring.deprecation is not None, "Deprecation information not found."
    if expected_depr_version is not None:
        assert docstring.deprecation.version == expected_depr_version, f"Expected version '{expected_depr_version}' but got '{docstring.deprecation.version}'"
    if expected_depr_desc is not None:
        assert docstring.deprecation.description == expected_depr_desc, f"Expected description '{expected_depr_desc}' but got '{docstring.deprecation.description}'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_info
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_info.py:7:27: E0602: Undefined variable 'T' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_info.py:8:24: E0602: Undefined variable 'T' (undefined-variable)


"""
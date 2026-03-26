
import pytest
from docstring_parser import parse
import typing as T

def test_deprecation(
    source: str,
    expected_depr_version: T.Optional[str],
    expected_depr_desc: T.Optional[str],
) -> None:
    """Test parsing deprecation notes from a given string.

    This function is designed to verify that the parsed docstring contains the expected deprecation information. It takes a string `source` containing potential deprecation notes and checks if the deprecation version (`expected_depr_version`) and description (`expected_depr_desc`) match those found in the provided source string.

    Parameters:
        source (str): The input string containing the docstring to be parsed. This should include any numpy-style docstring with potential deprecation notes.
        expected_depr_version (Optional[str]): The version number that is expected to be marked as deprecated, if present. This can be a string representing the version or None if no specific version is expected.
        expected_depr_desc (Optional[str]): A description of what is being deprecated, which could include information about why it was deprecated and any alternatives. This can also be a string or None if no specific description is expected.

    Returns:
        None

    Raises:
        AssertionError: If the parsed deprecation information does not match the expected values. This ensures that tests can catch any discrepancies between specified and actual deprecation details, which is crucial for maintaining accurate and up-to-date documentation.

    Examples:
        # Basic usage with expected deprecation notes
        test_deprecation("""
        Some function to demonstrate deprecation.
        
        Deprecated since version 1.0.0: Use another_function instead.
        """, "1.0.0", "Use another_function instead.")
        
        # No expected deprecation notes
        test_deprecation("""
        Some function to demonstrate no deprecation.
        """, None, None)
        
        # Incorrect expected deprecation notes
        try:
            test_deprecation("""
            Some function with incorrect deprecation note.
            
            Deprecated since version 2.0.0: Use another_function instead.
            """, "1.0.0", "Use another_function instead.")
        except AssertionError as e:
            print(e)  # Output will indicate a mismatch in expected and actual deprecation notes

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_valid_input.py:29:8: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_valid_input, line 29)' (syntax-error)


"""

import pytest
import typing as T
from docstring_parser.tests.test_numpydoc import ParametersSection, ReturnsSection
from docstring_parser import parse

def test_examples(source, expected_results: T.List[T.Tuple[T.Optional[str], str]]) -> None:
    """Test parsing examples by comparing the parsed results with the provided expected outcomes.

    This function takes a source code string and a list of tuples containing optional snippet strings and descriptions as expected results. It parses the docstring from the source code, then compares each example's snippet and description against the corresponding values in `expected_results`. If any mismatch is found, it raises an assertion error.

    Parameters:
        source (str): A string containing the source code from which to extract the docstring for testing.
        expected_results (List[Tuple[Optional[str], str]]): A list of tuples where each tuple contains an optional snippet string and a description string that are expected results for corresponding examples in the parsed docstring.

    Returns:
        None
    """
    docstring = parse(source)
    assert len(docstring.meta) == len(expected_results)
    for meta, expected_result in zip(docstring.meta, expected_results):
        assert meta.description == expected_result[1]
    assert len(docstring.examples) == len(expected_results)
    for example, expected_result in zip(docstring.examples, expected_results):
        assert example.snippet == expected_result[0]
        assert example.description == expected_result[1]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_input_custom_sections
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_input_custom_sections.py:4:0: E0611: No name 'ParametersSection' in module 'docstring_parser.tests.test_numpydoc' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_input_custom_sections.py:4:0: E0611: No name 'ReturnsSection' in module 'docstring_parser.tests.test_numpydoc' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_input_custom_sections.py:5:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""
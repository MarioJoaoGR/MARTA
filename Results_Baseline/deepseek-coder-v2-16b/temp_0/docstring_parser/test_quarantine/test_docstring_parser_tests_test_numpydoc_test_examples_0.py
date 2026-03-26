
# Module: docstring_parser.tests.test_numpydoc
import pytest
from docstring_parser import parse, ParametersSection, ReturnsSection
import typing as T

# Test cases for the function `test_examples`
def test_examples():
    # Basic usage with default sections
    source = """
    Test function to demonstrate parsing examples.
    
    This is a longer explanation of what this function does and how it works.
    
    Parameters:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
        
    Returns:
        type: Description of the return value.
    """
    expected_results = [
        (None, "Test function to demonstrate parsing examples."),
        (None, "This is a longer explanation of what this function does and how it works.")
    ]
    docstring = parse(source)
    assert len(docstring.meta) == len(expected_results)
    for meta, expected_result in zip(docstring.meta, expected_results):
        assert meta.description == expected_result[1]
    assert len(docstring.examples) == len(expected_results)
    for example, expected_result in zip(docstring.examples, expected_results):
        assert example.snippet == expected_result[0]
        assert example.description == expected_result[1]

    # Customizing sections to parse specific parts of the docstring
    custom_sections = {
        'Parameters': ParametersSection(),
        'Returns': ReturnsSection()
    }
    source = """
    Test function to demonstrate parsing examples.
    
    This is a longer explanation of what this function does and how it works.
    
    Parameters:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
        
    Returns:
        type: Description of the return value.
    """
    expected_results = [
        (None, "Test function to demonstrate parsing examples."),
        ("param1 (type): Description of param1.\nparam2 (type): Description of param2.", "This is a longer explanation of what this function does and how it works.")
    ]
    docstring = parse(source)
    assert len(docstring.meta) == len(expected_results)
    for meta, expected_result in zip(docstring.meta, expected_results):
        assert meta.description == expected_result[1]
    assert len(docstring.examples) == len(expected_results)
    for example, expected_result in zip(docstring.examples, expected_results):
        assert example.snippet == expected_result[0]
        assert example.description == expected_result[1]

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_examples_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0.py:4:0: E0611: No name 'ParametersSection' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0.py:4:0: E0611: No name 'ReturnsSection' in module 'docstring_parser' (no-name-in-module)

"""
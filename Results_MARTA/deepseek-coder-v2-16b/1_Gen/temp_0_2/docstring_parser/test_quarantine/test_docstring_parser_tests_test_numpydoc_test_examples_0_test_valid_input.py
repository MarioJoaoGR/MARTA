
import pytest
from docstring_parser import parse

def test_examples(source, expected_results: T.List[T.Tuple[T.Optional[str], str]]):
    """Test parsing examples by comparing the parsed results with the provided expected results."""
    docstring = parse(source)
    assert len(docstring.meta) == len(expected_results), f"Expected {len(expected_results)} meta items, but got {len(docstring.meta)}"
    for meta, expected_result in zip(docstring.meta, expected_results):
        assert meta.description == expected_result[1], f"Expected description '{expected_result[1]}', but got '{meta.description}'"
    assert len(docstring.examples) == len(expected_results), f"Expected {len(expected_results)} example items, but got {len(docstring.examples)}"
    for example, expected_result in zip(docstring.examples, expected_results):
        assert example.snippet == expected_result[0], f"Expected snippet '{expected_result[0]}', but got '{example.snippet}'"
        assert example.description == expected_result[1], f"Expected description '{expected_result[1]}', but got '{example.description}'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_input.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_input.py:5:44: E0602: Undefined variable 'T' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_input.py:5:51: E0602: Undefined variable 'T' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_input.py:5:59: E0602: Undefined variable 'T' (undefined-variable)


"""
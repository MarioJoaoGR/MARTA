
import pytest
from docstring_parser.tests.test_numpydoc import parse
import typing as T

@pytest.fixture(scope="module")
def source():
    return """
    Test function to demonstrate parsing examples.
    
    This is a longer explanation of what this function does and how it works.
    
    Parameters:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
        
    Returns:
        type: Description of the return value.
    """

@pytest.fixture(scope="module")
def expected_results():
    return [
        (None, "Test function to demonstrate parsing examples."),
        ("param1 (type): Description of param1.\nparam2 (type): Description of param2.", "This is a longer explanation of what this function does and how it works.")
    ]

def test_examples(source, expected_results: T.List[T.Tuple[T.Optional[str], str]]) -> None:
    """Test parsing examples by comparing the parsed results with the provided expected outcomes."""
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
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
________________________________ test_examples _________________________________

source = '\n    Test function to demonstrate parsing examples.\n    \n    This is a longer explanation of what this function do...   param2 (type): Description of param2.\n        \n    Returns:\n        type: Description of the return value.\n    '
expected_results = [(None, 'Test function to demonstrate parsing examples.'), ('param1 (type): Description of param1.\nparam2 (type): Description of param2.', 'This is a longer explanation of what this function does and how it works.')]

    def test_examples(source, expected_results: T.List[T.Tuple[T.Optional[str], str]]) -> None:
        """Test parsing examples by comparing the parsed results with the provided expected outcomes."""
        docstring = parse(source)
>       assert len(docstring.meta) == len(expected_results)
E       AssertionError: assert 0 == 2
E        +  where 0 = len([])
E        +    where [] = <docstring_parser.common.Docstring object at 0x10636ebf0>.meta
E        +  and   2 = len([(None, 'Test function to demonstrate parsing examples.'), ('param1 (type): Description of param1.\nparam2 (type): Description of param2.', 'This is a longer explanation of what this function does and how it works.')])

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_inputs.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_valid_inputs.py::test_examples
============================== 1 failed in 0.04s ===============================
"""
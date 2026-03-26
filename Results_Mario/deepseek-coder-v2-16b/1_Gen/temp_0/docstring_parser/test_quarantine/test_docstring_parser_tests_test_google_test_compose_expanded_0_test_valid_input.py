
import pytest
from docstring_parser.tests.test_google import parse, compose, RenderingStyle

@pytest.mark.parametrize("source, expected", [
    (
        "This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns: int: The result of the operation, which could be an integer.",
        """This is a summary.

Args:
    param1 (int): Description of parameter 1.
    param2 (str): Description of parameter 2.

Returns:
    int: The result of the operation, which could be an integer."""
    )
])
def test_compose_expanded(source: str, expected: str) -> None:
    assert compose(parse(source), rendering_style=RenderingStyle.EXPANDED) == expected

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_ test_compose_expanded[This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns: int: The result of the operation, which could be an integer.-This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.] _

source = 'This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns: int: The result of the operation, which could be an integer.'
expected = 'This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.'

    @pytest.mark.parametrize("source, expected", [
        (
            "This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns: int: The result of the operation, which could be an integer.",
            """This is a summary.
    
    Args:
        param1 (int): Description of parameter 1.
        param2 (str): Description of parameter 2.
    
    Returns:
        int: The result of the operation, which could be an integer."""
        )
    ])
    def test_compose_expanded(source: str, expected: str) -> None:
>       assert compose(parse(source), rendering_style=RenderingStyle.EXPANDED) == expected
E       AssertionError: assert 'This is a su... parameter 2.' == 'This is a su...e an integer.'
E         
E         Skipping 33 identical leading characters in diff, use -v to show
E         + am1 (int):
E         - am1 (int): Description of parameter 1.
E         ? ^^^^^^^^^^
E         +         Description of parameter 1.
E         ? ^^^^^^^...
E         
E         ...Full output truncated (8 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_valid_input.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_valid_input.py::test_compose_expanded[This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns: int: The result of the operation, which could be an integer.-This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.]
============================== 1 failed in 0.03s ===============================

"""
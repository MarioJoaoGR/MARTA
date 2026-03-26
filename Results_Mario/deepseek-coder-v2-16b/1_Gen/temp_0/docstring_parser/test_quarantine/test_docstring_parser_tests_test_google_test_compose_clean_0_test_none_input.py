
import pytest
from docstring_parser.tests.test_google import compose, parse, RenderingStyle

@pytest.fixture(scope="module")
def source():
    return """This is a summary.
    
    Args:
        param1 (int): Description of parameter 1.
        param2 (str): Description of parameter 2.
        
    Returns:
        int: The result of the operation, which could be an integer."""

@pytest.fixture(scope="module")
def expected():
    return "Expected formatted string"

def test_compose_clean(source, expected):
    assert (
        compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
    )

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_compose_clean ______________________________

source = 'This is a summary.\n    \n    Args:\n        param1 (int): Description of parameter 1.\n        param2 (str): Description of parameter 2.\n        \n    Returns:\n        int: The result of the operation, which could be an integer.'
expected = 'Expected formatted string'

    def test_compose_clean(source, expected):
>       assert (
            compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
        )
E       AssertionError: assert 'This is a su...e an integer.' == 'Expected formatted string'
E         
E         - Expected formatted string
E         + This is a summary.
E         + 
E         + Args:
E         +     param1 (int): Description of parameter 1.
E         +     param2 (str): Description of parameter 2....
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_0_test_none_input.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_0_test_none_input.py::test_compose_clean
============================== 1 failed in 0.03s ===============================

"""
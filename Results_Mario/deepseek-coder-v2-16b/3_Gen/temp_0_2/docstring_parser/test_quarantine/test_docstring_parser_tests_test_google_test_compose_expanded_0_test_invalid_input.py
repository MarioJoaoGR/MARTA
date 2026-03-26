
import pytest
from docstring_parser.tests.test_google import compose, parse, RenderingStyle

@pytest.fixture
def source():
    return """
    Example Google-style docstring:
    This is a sample function.
    
    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.
        
    Returns:
        None
    """

@pytest.fixture
def expected():
    return "Expected expanded format"

def test_compose_expanded(source, expected):
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
____________________________ test_compose_expanded _____________________________

source = '\n    Example Google-style docstring:\n    This is a sample function.\n    \n    Args:\n        param1 (int): Description of param1.\n        param2 (str): Description of param2.\n        \n    Returns:\n        None\n    '
expected = 'Expected expanded format'

    def test_compose_expanded(source, expected):
>       assert compose(parse(source), rendering_style=RenderingStyle.EXPANDED) == expected
E       AssertionError: assert 'Example Goog...n        None' == 'Expected expanded format'
E         
E         - Expected expanded format
E         + Example Google-style docstring:
E         + This is a sample function.
E         + 
E         + Args:
E         +     param1 (int):...
E         
E         ...Full output truncated (7 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_invalid_input.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_invalid_input.py::test_compose_expanded
============================== 1 failed in 0.04s ===============================
"""
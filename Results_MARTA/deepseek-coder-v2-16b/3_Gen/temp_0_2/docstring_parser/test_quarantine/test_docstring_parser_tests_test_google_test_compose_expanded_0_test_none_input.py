
import pytest
from docstring_parser.tests.test_google import compose, parse, RenderingStyle

@pytest.fixture(scope="module")
def source():
    return """
    Example Google-style docstring.
    
    This is a multi-line description that explains what the function does.
    
    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.
    
    Returns:
        bool: The return value. True for success, False otherwise.
    """

@pytest.fixture(scope="module")
def expected():
    return "Example Google-style docstring.\n\nThis is a multi-line description that explains what the function does.\n\nArgs:\n    param1 (int): Description of param1.\n    param2 (str): Description of param2.\n\nReturns:\n    bool: The return value. True for success, False otherwise."

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
____________________________ test_compose_expanded _____________________________

source = '\n    Example Google-style docstring.\n    \n    This is a multi-line description that explains what the function doe...: Description of param2.\n    \n    Returns:\n        bool: The return value. True for success, False otherwise.\n    '
expected = 'Example Google-style docstring.\n\nThis is a multi-line description that explains what the function does.\n\nArgs:\n ...\n    param2 (str): Description of param2.\n\nReturns:\n    bool: The return value. True for success, False otherwise.'

    def test_compose_expanded(source, expected):
>       assert compose(parse(source), rendering_style=RenderingStyle.EXPANDED) == expected
E       AssertionError: assert 'Example Goog...se otherwise.' == 'Example Goog...se otherwise.'
E         
E         Skipping 118 identical leading characters in diff, use -v to show
E         - am1 (int): Description of param1.
E         + am1 (int):
E         +         Description of param1.
E         +     param2 (str):
E         -     param2 (str): Description of param2....
E         
E         ...Full output truncated (10 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_none_input.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_none_input.py::test_compose_expanded
============================== 1 failed in 0.04s ===============================
"""
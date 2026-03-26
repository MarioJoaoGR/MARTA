
import pytest
from docstring_parser.tests.test_google import parse, compose, RenderingStyle

@pytest.fixture(params=[
    ("This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns: int: The result of the operation, which could be an integer.",
     """This is a summary.

Args:
    param1 (int): Description of parameter 1.
    param2 (str): Description of parameter 2.

Returns:
    int: The result of the operation, which could be an integer."""),
])
def source_and_expected(request):
    return request.param

def test_compose_expanded(source_and_expected):
    source, expected = source_and_expected
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_________________ test_compose_expanded[source_and_expected0] __________________

source_and_expected = ('This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of paramet...ram2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.')

    def test_compose_expanded(source_and_expected):
        source, expected = source_and_expected
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_edge_case_none.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_edge_case_none.py::test_compose_expanded[source_and_expected0]
============================== 1 failed in 0.03s ===============================
"""
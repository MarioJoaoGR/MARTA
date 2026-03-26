
import pytest
from docstring_parser.tests.test_google import compose, parse, RenderingStyle

@pytest.mark.parametrize("source, expected", [
    ('Valid docstring', "Expected expanded format")
])
def test_compose_expanded(source, expected):
    """Test the composition of a parsed docstring in expanded mode."""
    assert (
        compose(parse(source), rendering_style=RenderingStyle.EXPANDED)
        == expected
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______ test_compose_expanded[Valid docstring-Expected expanded format] ________

source = 'Valid docstring', expected = 'Expected expanded format'

    @pytest.mark.parametrize("source, expected", [
        ('Valid docstring', "Expected expanded format")
    ])
    def test_compose_expanded(source, expected):
        """Test the composition of a parsed docstring in expanded mode."""
>       assert (
            compose(parse(source), rendering_style=RenderingStyle.EXPANDED)
            == expected
        )
E       AssertionError: assert 'Valid docstring' == 'Expected expanded format'
E         
E         - Expected expanded format
E         + Valid docstring

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_expanded_0_test_valid_input.py::test_compose_expanded[Valid docstring-Expected expanded format]
============================== 1 failed in 0.04s ===============================
"""
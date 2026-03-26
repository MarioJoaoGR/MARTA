
import pytest
from docstring_parser.tests.test_rest import parse, compose, RenderingStyle

@pytest.fixture(params=[RenderingStyle.COMPACT, RenderingStyle.EXPANDED])
def test_compose(request):
    rendering_style = request.param
    expected = "Expected output" if rendering_style == RenderingStyle.COMPACT else "Expected expanded output"
    
    docstring = parse(
        """
        Short description.

        Long description.

        :param int foo: a description
        :param int bar: another description
        :return float: a return
        """
    )
    assert compose(docstring, rendering_style=rendering_style) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.03s =============================
"""
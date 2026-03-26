
import pytest
from docstring_parser.tests.test_numpydoc import parse

@pytest.fixture(params=[
    ("A brief description of what this function does.\n\nExtended documentation or explanation follows here.", "A brief description of what this function does.", "Extended documentation or explanation follows here.", True),
    ("A brief description of what this function does.\n\nExtended documentation or explanation follows here.\n\nParameters:\n    param1 (type): Description of param1.\n    param2 (type): Description of param2.\n\nReturns:\n    type: Description of the return value.", "A brief description of what this function does.", "Extended documentation or explanation follows here.", True)
])
def test_long_description(request):
    source, expected_short_desc, expected_long_desc, expected_blank = request.param
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank
    assert not docstring.meta

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
============================ no tests ran in 0.02s =============================
"""
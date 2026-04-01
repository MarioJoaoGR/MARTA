
import pytest
from docstring_parser.tests.test_numpydoc import parse

@pytest.fixture(params=[
    ("def example(param1: int = 5): pass", False, "int", "5"),
    ("def example(param1 = None): pass", True, None, "None"),
    ("def example(param1: int): pass", False, "int", None),
])
def test_default_args(request):
    source, expected_is_optional, expected_type_name, expected_default = request.param
    docstring = parse(source)
    assert docstring is not None
    assert len(docstring.params) == 1

    arg1 = docstring.params[0]
    assert arg1.is_optional == expected_is_optional
    assert arg1.type_name == expected_type_name
    assert arg1.default == expected_default

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
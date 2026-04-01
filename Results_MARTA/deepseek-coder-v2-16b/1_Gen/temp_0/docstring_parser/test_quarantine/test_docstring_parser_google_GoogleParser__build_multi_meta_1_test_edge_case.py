
import pytest
from docstring_parser.google import GoogleParser, Section

@pytest.fixture
def parser():
    return GoogleParser(sections=[Section('param', 'Parameter description')], title_colon=True)

def test_parser_initialization(parser):
    assert isinstance(parser, GoogleParser)
    assert parser.title_colon is True
    assert len(parser.sections) == 1
    assert list(parser.sections.keys())[0] == 'param'
    assert parser.sections['param'].description == 'Parameter description'

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

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_1_test_edge_case.py E [100%]

==================================== ERRORS ====================================
_________________ ERROR at setup of test_parser_initialization _________________

    @pytest.fixture
    def parser():
>       return GoogleParser(sections=[Section('param', 'Parameter description')], title_colon=True)
E       TypeError: SectionBase.__new__() missing 1 required positional argument: 'type'

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_1_test_edge_case.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_1_test_edge_case.py::test_parser_initialization
=============================== 1 error in 0.03s ===============================

"""
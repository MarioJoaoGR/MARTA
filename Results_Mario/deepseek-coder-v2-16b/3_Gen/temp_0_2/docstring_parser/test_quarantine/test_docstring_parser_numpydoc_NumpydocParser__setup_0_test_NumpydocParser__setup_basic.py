
import re
from docstring_parser.numpydoc import NumpydocParser, DEFAULT_SECTIONS, Section

def test_NumpydocParser__setup_basic():
    parser = NumpydocParser()
    
    # Check that the default sections are set up correctly
    assert len(parser.sections) == len(DEFAULT_SECTIONS)
    for section in DEFAULT_SECTIONS:
        assert section.title in parser.sections
        assert re.match(section.title_pattern, "", re.M) is not None

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

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser__setup_0_test_NumpydocParser__setup_basic.py F [100%]

=================================== FAILURES ===================================
_______________________ test_NumpydocParser__setup_basic _______________________

    def test_NumpydocParser__setup_basic():
        parser = NumpydocParser()
    
        # Check that the default sections are set up correctly
        assert len(parser.sections) == len(DEFAULT_SECTIONS)
        for section in DEFAULT_SECTIONS:
            assert section.title in parser.sections
>           assert re.match(section.title_pattern, "", re.M) is not None
E           AssertionError: assert None is not None
E            +  where None = <function match at 0x100bed900>('^(Parameters)\\s*?\\n----------\\s*$', '', re.MULTILINE)
E            +    where <function match at 0x100bed900> = re.match
E            +    and   '^(Parameters)\\s*?\\n----------\\s*$' = <docstring_parser.numpydoc.ParamSection object at 0x101f91810>.title_pattern
E            +    and   re.MULTILINE = re.M

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser__setup_0_test_NumpydocParser__setup_basic.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser__setup_0_test_NumpydocParser__setup_basic.py::test_NumpydocParser__setup_basic
============================== 1 failed in 0.03s ===============================
"""
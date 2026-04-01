
import pytest
from docstring_parser.common import Docstring, DocstringReturns

class MockDocstringReturns:
    pass

def test_many_returns():
    doc = Docstring()
    
    # Adding a mock DocstringReturns instance to meta for testing
    mock_return = MockDocstringReturns()
    doc.meta.append(mock_return)
    
    # Checking if the method returns a list containing only the mocked return value
    assert len([item for item in doc.many_returns() if isinstance(item, MockDocstringReturns)]) == 1

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

docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_many_returns_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_many_returns _______________________________

    def test_many_returns():
        doc = Docstring()
    
        # Adding a mock DocstringReturns instance to meta for testing
        mock_return = MockDocstringReturns()
        doc.meta.append(mock_return)
    
        # Checking if the method returns a list containing only the mocked return value
>       assert len([item for item in doc.many_returns() if isinstance(item, MockDocstringReturns)]) == 1
E       TypeError: 'list' object is not callable

docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_many_returns_0_test_invalid_inputs.py:16: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_many_returns_0_test_invalid_inputs.py::test_many_returns
============================== 1 failed in 0.02s ===============================
"""
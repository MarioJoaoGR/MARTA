
import pytest
from docstring_parser.tests.test_rest import parse

def test_invalid_input():
    source = 12345
    with pytest.raises(AssertionError):
        docstring = parse(source)

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        source = 12345
        with pytest.raises(AssertionError):
>           docstring = parse(source)

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
docstring_parser/docstring_parser/rest.py:111: in parse
    text = inspect.cleandoc(text)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

doc = 12345

    def cleandoc(doc):
        """Clean up indentation from docstrings.
    
        Any whitespace that can be uniformly removed from the second line
        onwards is removed."""
        try:
>           lines = doc.expandtabs().split('\n')
E           AttributeError: 'int' object has no attribute 'expandtabs'

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:750: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""
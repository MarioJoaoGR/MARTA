
import pytest
from docstring_parser.tests.test_google import parse

def test_invalid_input_error_handling():
    with pytest.raises(TypeError):
        parse(12345)

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        with pytest.raises(TypeError):
>           parse(12345)

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_invalid_input_error_handling.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
docstring_parser/docstring_parser/google.py:301: in parse
    return GoogleParser().parse(text)
docstring_parser/docstring_parser/google.py:215: in parse
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
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_invalid_input_error_handling.py::test_invalid_input_error_handling
============================== 1 failed in 0.06s ===============================
"""

import pytest
from docstring_parser.tests.test_google import parse

@pytest.fixture
def source():
    return """
    def example():
        \"\"\"
        This is a summary.
        
        Args:
            arg1 (int): The first argument.
            arg2 (str): The second argument.
            
        Returns:
            int: The result of the function.
        \"\"\"
    """

@pytest.fixture
def expected_short_desc():
    return "This is a summary."

@pytest.fixture
def expected_long_desc():
    return "Args:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\nReturns:\n    int: The result of the function."

@pytest.fixture
def expected_blank():
    return True

def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
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
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
____________________________ test_long_description _____________________________

source = '\n    def example():\n        """\n        This is a summary.\n        \n        Args:\n            arg1 (int): The f... The second argument.\n            \n        Returns:\n            int: The result of the function.\n        """\n    '
expected_short_desc = 'This is a summary.'
expected_long_desc = 'Args:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\nReturns:\n    int: The result of the function.'
expected_blank = True

    def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
        docstring = parse(source)
>       assert docstring.short_description == expected_short_desc
E       AssertionError: assert 'def example():' == 'This is a summary.'
E         
E         - This is a summary.
E         + def example():

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_0_test_invalid_input.py:35: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_0_test_invalid_input.py::test_long_description
============================== 1 failed in 0.03s ===============================
"""
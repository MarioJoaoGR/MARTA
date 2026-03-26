
import pytest
from docstring_parser.tests.test_google import parse

@pytest.fixture(params=[
    ("""
    def example():
        \"\"\"
        This is a summary.
        
        Args:
            arg1 (int): The first argument.
            arg2 (str): The second argument.
            
        Returns:
            int: The result of the function.
        \"\"\"
    """, "This is a summary.", "Args:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\nReturns:\n    int: The result of the function.", False, False),
])
def test_meta_newlines(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc):
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank_short_desc
    assert docstring.blank_after_long_description == expected_blank_long_desc
    assert len(docstring.meta) == 1

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
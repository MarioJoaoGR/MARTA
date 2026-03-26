
import pytest
from docstring_parser import parse

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
    ("This is a summary.\n\nThis is the long description.", "This is a summary.", "This is the long description.", True),
    ("This is a summary. This is the long description.", "This is a summary.", "This is the long description.", False),
    ("", None, None, False)
])
def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
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
collected 3 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_2.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_ test_long_description[This is a summary. This is the long description.-This is a summary.-This is the long description.-False] _

source = 'This is a summary. This is the long description.'
expected_short_desc = 'This is a summary.'
expected_long_desc = 'This is the long description.', expected_blank = False

    @pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
        ("This is a summary.\n\nThis is the long description.", "This is a summary.", "This is the long description.", True),
        ("This is a summary. This is the long description.", "This is a summary.", "This is the long description.", False),
        ("", None, None, False)
    ])
    def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
        docstring = parse(source)
>       assert docstring.short_description == expected_short_desc
E       AssertionError: assert 'This is a su... description.' == 'This is a summary.'
E         
E         - This is a summary.
E         + This is a summary. This is the long description.

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_2.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_2.py::test_long_description[This is a summary. This is the long description.-This is a summary.-This is the long description.-False]
========================= 1 failed, 2 passed in 0.02s ==========================

"""
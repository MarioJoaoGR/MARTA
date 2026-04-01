
import pytest
from docstring_parser.tests.test_rest import parse

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
    (None, "This is a brief description.", "And this is more detailed documentation.", False)
])
def test_edge_case(source, expected_short_desc, expected_long_desc, expected_blank):
    """Test parsing long description."""
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_ test_edge_case[None-This is a brief description.-And this is more detailed documentation.-False] _

source = None, expected_short_desc = 'This is a brief description.'
expected_long_desc = 'And this is more detailed documentation.'
expected_blank = False

    @pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
        (None, "This is a brief description.", "And this is more detailed documentation.", False)
    ])
    def test_edge_case(source, expected_short_desc, expected_long_desc, expected_blank):
        """Test parsing long description."""
        docstring = parse(source)
>       assert docstring.short_description == expected_short_desc
E       AssertionError: assert None == 'This is a brief description.'
E        +  where None = <docstring_parser.common.Docstring object at 0x102adac80>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case.py::test_edge_case[None-This is a brief description.-And this is more detailed documentation.-False]
============================== 1 failed in 0.08s ===============================
"""
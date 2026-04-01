
import pytest
from docstring_parser.tests.test_rest import parse

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
    ("This is a brief description.\n\nHere is a more detailed explanation.", "This is a brief description.", "Here is a more detailed explanation.", True),
    (":param arg: This is a parameter.\n:type arg: int", None, "This is a parameter.", False),
    (":returns: This function returns an integer.\n:rtype: int", None, "This function returns an integer.", True)
])
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
collected 3 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case_no_descriptions.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_ test_long_description[:param arg: This is a parameter.\n:type arg: int-None-This is a parameter.-False] _

source = ':param arg: This is a parameter.\n:type arg: int'
expected_short_desc = None, expected_long_desc = 'This is a parameter.'
expected_blank = False

    @pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
        ("This is a brief description.\n\nHere is a more detailed explanation.", "This is a brief description.", "Here is a more detailed explanation.", True),
        (":param arg: This is a parameter.\n:type arg: int", None, "This is a parameter.", False),
        (":returns: This function returns an integer.\n:rtype: int", None, "This function returns an integer.", True)
    ])
    def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
        docstring = parse(source)
        assert docstring.short_description == expected_short_desc
>       assert docstring.long_description == expected_long_desc
E       AssertionError: assert None == 'This is a parameter.'
E        +  where None = <docstring_parser.common.Docstring object at 0x11028cc40>.long_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case_no_descriptions.py:13: AssertionError
_ test_long_description[:returns: This function returns an integer.\n:rtype: int-None-This function returns an integer.-True] _

source = ':returns: This function returns an integer.\n:rtype: int'
expected_short_desc = None
expected_long_desc = 'This function returns an integer.', expected_blank = True

    @pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
        ("This is a brief description.\n\nHere is a more detailed explanation.", "This is a brief description.", "Here is a more detailed explanation.", True),
        (":param arg: This is a parameter.\n:type arg: int", None, "This is a parameter.", False),
        (":returns: This function returns an integer.\n:rtype: int", None, "This function returns an integer.", True)
    ])
    def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
        docstring = parse(source)
        assert docstring.short_description == expected_short_desc
>       assert docstring.long_description == expected_long_desc
E       AssertionError: assert None == 'This function returns an integer.'
E        +  where None = <docstring_parser.common.Docstring object at 0x11028e800>.long_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case_no_descriptions.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case_no_descriptions.py::test_long_description[:param arg: This is a parameter.\n:type arg: int-None-This is a parameter.-False]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case_no_descriptions.py::test_long_description[:returns: This function returns an integer.\n:rtype: int-None-This function returns an integer.-True]
========================= 2 failed, 1 passed in 0.04s ==========================
"""

import pytest
from docstring_parser.tests.test_rest import parse

@pytest.fixture(params=[
    ("This is a brief description.\n\nAnd this is more detailed documentation.", "This is a brief description.", "And this is more detailed documentation.", False),
    # Add more test cases as needed
])
def source_expected_descs(request):
    return request.param

def test_long_description(source_expected_descs):
    source, expected_short_desc, expected_long_desc, expected_blank = source_expected_descs
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
________________ test_long_description[source_expected_descs0] _________________

source_expected_descs = ('This is a brief description.\n\nAnd this is more detailed documentation.', 'This is a brief description.', 'And this is more detailed documentation.', False)

    def test_long_description(source_expected_descs):
        source, expected_short_desc, expected_long_desc, expected_blank = source_expected_descs
        docstring = parse(source)
        assert docstring.short_description == expected_short_desc
        assert docstring.long_description == expected_long_desc
>       assert docstring.blank_after_short_description == expected_blank
E       assert True == False
E        +  where True = <docstring_parser.common.Docstring object at 0x104826e60>.blank_after_short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_valid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_valid_input.py::test_long_description[source_expected_descs0]
============================== 1 failed in 0.07s ===============================
"""
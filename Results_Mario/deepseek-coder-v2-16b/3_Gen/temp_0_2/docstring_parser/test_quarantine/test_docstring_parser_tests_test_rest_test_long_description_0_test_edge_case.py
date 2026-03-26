
import pytest
from docstring_parser.tests.test_rest import parse

@pytest.fixture(params=[
    ("This is a short description.\n\nHere is a longer description.", "This is a short description.", "Here is a longer description.", True),
    (":param param1: Description of param1.\n:type param1: int\n:return: The result of the operation.", None, "Description of param1.", False)
])
def source_fixture(request):
    return request.param

def test_long_description(source_fixture):
    source, expected_short_desc, expected_long_desc, expected_blank = source_fixture
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
collected 2 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________ test_long_description[source_fixture1] ____________________

source_fixture = (':param param1: Description of param1.\n:type param1: int\n:return: The result of the operation.', None, 'Description of param1.', False)

    def test_long_description(source_fixture):
        source, expected_short_desc, expected_long_desc, expected_blank = source_fixture
        docstring = parse(source)
        assert docstring.short_description == expected_short_desc
>       assert docstring.long_description == expected_long_desc
E       AssertionError: assert None == 'Description of param1.'
E        +  where None = <docstring_parser.common.Docstring object at 0x1049df610>.long_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0_test_edge_case.py::test_long_description[source_fixture1]
========================= 1 failed, 1 passed in 0.04s ==========================
"""
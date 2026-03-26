
import pytest
from docstring_parser.tests.test_epydoc import parse

@pytest.fixture(params=[
    ("@param param_name: Description of the parameter.\n@return: The result of the function.", "Description of the parameter.", "The result of the function.", True, False),
    ("@param param_name: Description of the parameter.\n\n@return: The result of the function.", "Description of the parameter.", "The result of the function.", False, False),
    ("@param param_name: Description of the parameter.\n\n@return: The result of the function.\n", "Description of the parameter.", "The result of the function.", True, True)
])
def test_data(request):
    return request.param

def test_meta_newlines(test_data):
    source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc = test_data
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
collected 3 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_newlines_0_test_valid_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_meta_newlines[test_data0] ________________________

test_data = ('@param param_name: Description of the parameter.\n@return: The result of the function.', 'Description of the parameter.', 'The result of the function.', True, False)

    def test_meta_newlines(test_data):
        source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc = test_data
        docstring = parse(source)
>       assert docstring.short_description == expected_short_desc
E       AssertionError: assert None == 'Description of the parameter.'
E        +  where None = <docstring_parser.common.Docstring object at 0x106039d80>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_newlines_0_test_valid_input.py:16: AssertionError
________________________ test_meta_newlines[test_data1] ________________________

test_data = ('@param param_name: Description of the parameter.\n\n@return: The result of the function.', 'Description of the parameter.', 'The result of the function.', False, False)

    def test_meta_newlines(test_data):
        source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc = test_data
        docstring = parse(source)
>       assert docstring.short_description == expected_short_desc
E       AssertionError: assert None == 'Description of the parameter.'
E        +  where None = <docstring_parser.common.Docstring object at 0x106077b50>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_newlines_0_test_valid_input.py:16: AssertionError
________________________ test_meta_newlines[test_data2] ________________________

test_data = ('@param param_name: Description of the parameter.\n\n@return: The result of the function.\n', 'Description of the parameter.', 'The result of the function.', True, True)

    def test_meta_newlines(test_data):
        source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc = test_data
        docstring = parse(source)
>       assert docstring.short_description == expected_short_desc
E       AssertionError: assert None == 'Description of the parameter.'
E        +  where None = <docstring_parser.common.Docstring object at 0x106074580>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_newlines_0_test_valid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_newlines_0_test_valid_input.py::test_meta_newlines[test_data0]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_newlines_0_test_valid_input.py::test_meta_newlines[test_data1]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_newlines_0_test_valid_input.py::test_meta_newlines[test_data2]
============================== 3 failed in 0.03s ===============================
"""
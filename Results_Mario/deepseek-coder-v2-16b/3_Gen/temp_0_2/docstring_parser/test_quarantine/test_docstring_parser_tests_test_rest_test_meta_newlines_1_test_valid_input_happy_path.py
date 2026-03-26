
import pytest
from docstring_parser.tests.test_rest import parse

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc", [
    ("This is a short description.\n\nHere is a longer description.", "This is a short description.", "Here is a longer description.", True, True, "This is a short description.\n\nHere is a longer description."),
    (":param param1: Description of param1.\n:type param1: int\n:return: The result of the operation.", None, "The result of the operation.", True, False, "Description of param1.")
])
def test_meta_newlines(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc):
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank_short_desc
    assert docstring.blank_after_long_description == expected_blank_long_desc
    assert docstring.description == expected_full_desc

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_1_test_valid_input_happy_path.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_ test_meta_newlines[This is a short description.\n\nHere is a longer description.-This is a short description.-Here is a longer description.-True-True-This is a short description.\n\nHere is a longer description.] _

source = 'This is a short description.\n\nHere is a longer description.'
expected_short_desc = 'This is a short description.'
expected_long_desc = 'Here is a longer description.'
expected_blank_short_desc = True, expected_blank_long_desc = True
expected_full_desc = 'This is a short description.\n\nHere is a longer description.'

    @pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc", [
        ("This is a short description.\n\nHere is a longer description.", "This is a short description.", "Here is a longer description.", True, True, "This is a short description.\n\nHere is a longer description."),
        (":param param1: Description of param1.\n:type param1: int\n:return: The result of the operation.", None, "The result of the operation.", True, False, "Description of param1.")
    ])
    def test_meta_newlines(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc):
        docstring = parse(source)
        assert docstring.short_description == expected_short_desc
        assert docstring.long_description == expected_long_desc
        assert docstring.blank_after_short_description == expected_blank_short_desc
>       assert docstring.blank_after_long_description == expected_blank_long_desc
E       assert False == True
E        +  where False = <docstring_parser.common.Docstring object at 0x103e226b0>.blank_after_long_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_1_test_valid_input_happy_path.py:14: AssertionError
_ test_meta_newlines[:param param1: Description of param1.\n:type param1: int\n:return: The result of the operation.-None-The result of the operation.-True-False-Description of param1.] _

source = ':param param1: Description of param1.\n:type param1: int\n:return: The result of the operation.'
expected_short_desc = None, expected_long_desc = 'The result of the operation.'
expected_blank_short_desc = True, expected_blank_long_desc = False
expected_full_desc = 'Description of param1.'

    @pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc", [
        ("This is a short description.\n\nHere is a longer description.", "This is a short description.", "Here is a longer description.", True, True, "This is a short description.\n\nHere is a longer description."),
        (":param param1: Description of param1.\n:type param1: int\n:return: The result of the operation.", None, "The result of the operation.", True, False, "Description of param1.")
    ])
    def test_meta_newlines(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc):
        docstring = parse(source)
        assert docstring.short_description == expected_short_desc
>       assert docstring.long_description == expected_long_desc
E       AssertionError: assert None == 'The result of the operation.'
E        +  where None = <docstring_parser.common.Docstring object at 0x10446bd90>.long_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_1_test_valid_input_happy_path.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_1_test_valid_input_happy_path.py::test_meta_newlines[This is a short description.\n\nHere is a longer description.-This is a short description.-Here is a longer description.-True-True-This is a short description.\n\nHere is a longer description.]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_1_test_valid_input_happy_path.py::test_meta_newlines[:param param1: Description of param1.\n:type param1: int\n:return: The result of the operation.-None-The result of the operation.-True-False-Description of param1.]
============================== 2 failed in 0.04s ===============================
"""
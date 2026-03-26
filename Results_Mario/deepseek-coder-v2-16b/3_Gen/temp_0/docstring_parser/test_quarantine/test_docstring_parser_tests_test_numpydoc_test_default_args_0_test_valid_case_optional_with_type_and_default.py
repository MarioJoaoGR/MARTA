
import pytest
from docstring_parser.tests.test_numpydoc import parse
import typing as T

@pytest.fixture(params=[
    ("def example(param1: int = 5):\n    pass", False, "int", "5"),
    ("def example(param1 = None):\n    pass", True, None, "None"),
    ("def example(param1: int):\n    pass", False, "int", None)
])
def source_fixture(request):
    return request.param

def test_default_args(source_fixture):
    source, expected_is_optional, expected_type_name, expected_default = source_fixture
    docstring = parse(source)
    assert docstring is not None
    assert len(docstring.params) == 1

    arg1 = docstring.params[0]
    assert arg1.is_optional == expected_is_optional
    assert arg1.type_name == expected_type_name
    assert arg1.default == expected_default

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_valid_case_optional_with_type_and_default.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_default_args[source_fixture0] ______________________

source_fixture = ('def example(param1: int = 5):\n    pass', False, 'int', '5')

    def test_default_args(source_fixture):
        source, expected_is_optional, expected_type_name, expected_default = source_fixture
        docstring = parse(source)
        assert docstring is not None
>       assert len(docstring.params) == 1
E       assert 0 == 1
E        +  where 0 = len([])
E        +    where [] = <docstring_parser.common.Docstring object at 0x104a0f130>.params

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_valid_case_optional_with_type_and_default.py:18: AssertionError
______________________ test_default_args[source_fixture1] ______________________

source_fixture = ('def example(param1 = None):\n    pass', True, None, 'None')

    def test_default_args(source_fixture):
        source, expected_is_optional, expected_type_name, expected_default = source_fixture
        docstring = parse(source)
        assert docstring is not None
>       assert len(docstring.params) == 1
E       assert 0 == 1
E        +  where 0 = len([])
E        +    where [] = <docstring_parser.common.Docstring object at 0x104a3b430>.params

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_valid_case_optional_with_type_and_default.py:18: AssertionError
______________________ test_default_args[source_fixture2] ______________________

source_fixture = ('def example(param1: int):\n    pass', False, 'int', None)

    def test_default_args(source_fixture):
        source, expected_is_optional, expected_type_name, expected_default = source_fixture
        docstring = parse(source)
        assert docstring is not None
>       assert len(docstring.params) == 1
E       assert 0 == 1
E        +  where 0 = len([])
E        +    where [] = <docstring_parser.common.Docstring object at 0x104967e20>.params

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_valid_case_optional_with_type_and_default.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_valid_case_optional_with_type_and_default.py::test_default_args[source_fixture0]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_valid_case_optional_with_type_and_default.py::test_default_args[source_fixture1]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_valid_case_optional_with_type_and_default.py::test_default_args[source_fixture2]
============================== 3 failed in 0.07s ===============================
"""
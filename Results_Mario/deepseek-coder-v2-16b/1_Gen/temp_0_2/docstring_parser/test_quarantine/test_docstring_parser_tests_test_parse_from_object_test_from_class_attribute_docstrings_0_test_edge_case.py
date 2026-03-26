
import pytest
from docstring_parser.tests.test_parse_from_object import parse_from_object

def test_from_class_attribute_docstrings() -> None:
    """Test the parsing of attribute docstrings from a class."""

    class StandardCase:
        """Short description
        Long description
        """

        attr_one: str
        """Description for attr_one"""
        attr_two: bool = False
        """Description for attr_two"""

    docstring = parse_from_object(StandardCase)

    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description"
    assert docstring.description == "Short description\nLong description"
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "attr_one"
    assert docstring.params[0].type_name == "str"
    assert docstring.params[0].description == "Description for attr_one"
    assert docstring.params[1].arg_name == "attr_two"
    assert docstring.params[1].type_name == "bool"
    assert docstring.params[1].description == "Description for attr_two"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_0_test_edge_case.py _
ImportError while importing test module '/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_0_test_edge_case.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_0_test_edge_case.py:3: in <module>
    from docstring_parser.tests.test_parse_from_object import parse_from_object
docstring_parser/docstring_parser/tests/test_parse_from_object.py:5: in <module>
    from docstring_parser import parse_from_object
E   ImportError: cannot import name 'parse_from_object' from 'docstring_parser' (unknown location)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.07s ===============================
"""
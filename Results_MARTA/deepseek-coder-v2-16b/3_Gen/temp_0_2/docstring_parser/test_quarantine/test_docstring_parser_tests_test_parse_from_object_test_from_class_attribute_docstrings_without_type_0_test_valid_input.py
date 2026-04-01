
import pytest
from docstring_parser.tests.test_parse_from_object import parse_from_object

def test_from_class_attribute_docstrings_without_type() -> None:
    """Test the parse of untyped attribute docstrings."""

    class WithoutType:  # pylint: disable=missing-class-docstring
        attr_one = "value"
        """Description for attr_one"""

    docstring = parse_from_object(WithoutType)

    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.description is None
    assert len(docstring.params) == 1
    assert docstring.params[0].arg_name == "attr_one"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "Description for attr_one"

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
_ ERROR collecting Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_0_test_valid_input.py _
ImportError while importing test module '/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_0_test_valid_input.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_0_test_valid_input.py:3: in <module>
    from docstring_parser.tests.test_parse_from_object import parse_from_object
docstring_parser/docstring_parser/tests/test_parse_from_object.py:5: in <module>
    from docstring_parser import parse_from_object
E   ImportError: cannot import name 'parse_from_object' from 'docstring_parser' (unknown location)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.05s ===============================
"""
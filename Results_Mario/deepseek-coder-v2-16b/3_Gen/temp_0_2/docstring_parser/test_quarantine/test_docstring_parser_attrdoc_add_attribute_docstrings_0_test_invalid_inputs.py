
import pytest
from docstring_parser.attrdoc import add_attribute_docstrings, Docstring

def test_invalid_inputs():
    # Test with invalid types for obj and docstring
    with pytest.raises(TypeError):
        add_attribute_docstrings('invalid', 1234)

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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_add_attribute_docstrings_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with invalid types for obj and docstring
        with pytest.raises(TypeError):
>           add_attribute_docstrings('invalid', 1234)

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_add_attribute_docstrings_0_test_invalid_inputs.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

obj = 'invalid', docstring = 1234

    def add_attribute_docstrings(
        obj: T.Union[type, ModuleType], docstring: Docstring
    ) -> None:
        """Add attribute docstrings found in the object's source code.
    
        :param obj: object from which to parse attribute docstrings
        :param docstring: Docstring object where found attributes are added
        :returns: list with names of added attributes
        """
>       params = set(p.arg_name for p in docstring.params)
E       AttributeError: 'int' object has no attribute 'params'

docstring_parser/docstring_parser/attrdoc.py:113: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_add_attribute_docstrings_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.04s ===============================
"""
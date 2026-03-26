
import ast
import pytest
from docstring_parser.attrdoc import AttributeDocstrings

def test_valid_case():
    class MyClass:
        attr1: int = 10
        attr2: str = "hello"
    
    # Ensure the docstring is a multi-line string
    myclass_doc = "\n".join([f"{line}\n" for line in MyClass.__doc__.splitlines()]) if MyClass.__doc__ else ""
    
    module = ast.parse(myclass_doc)
    visitor = AttributeDocstrings()
    visitor.visit(module)
    
    assert len(visitor.attr_docs) == 2, "Expected two attributes to be parsed"

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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        class MyClass:
            attr1: int = 10
            attr2: str = "hello"
    
        # Ensure the docstring is a multi-line string
        myclass_doc = "\n".join([f"{line}\n" for line in MyClass.__doc__.splitlines()]) if MyClass.__doc__ else ""
    
        module = ast.parse(myclass_doc)
        visitor = AttributeDocstrings()
        visitor.visit(module)
    
>       assert len(visitor.attr_docs) == 2, "Expected two attributes to be parsed"
E       TypeError: object of type 'NoneType' has no len()

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_case.py:18: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.04s ===============================
"""
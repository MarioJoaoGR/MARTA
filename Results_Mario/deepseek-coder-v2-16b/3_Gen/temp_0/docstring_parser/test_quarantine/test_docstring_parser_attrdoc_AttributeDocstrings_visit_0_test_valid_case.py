
import ast
from docstring_parser.attrdoc import AttributeDocstrings

def test_valid_case():
    example_module = ast.parse('class MyClass:\n    attr: str = \'default\'')
    
    visitor = AttributeDocstrings()
    visitor.visit(example_module)
    
    assert 'attr' in visitor.attr_docs

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
        example_module = ast.parse('class MyClass:\n    attr: str = \'default\'')
    
        visitor = AttributeDocstrings()
        visitor.visit(example_module)
    
>       assert 'attr' in visitor.attr_docs
E       TypeError: argument of type 'NoneType' is not iterable

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_case.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.03s ===============================
"""

import ast
from docstring_parser.attrdoc import AttributeDocstrings

def test_valid_input():
    class_node = ast.ClassDef(name='ExampleClass', body=[
        ast.Assign(targets=[ast.Name(id='attr1')], value=ast.Constant(value="42")),
        ast.Assign(targets=[ast.Name(id='attr2')], value=ast.Constant(value='"string"'))
    ])
    
    attr_visitor = AttributeDocstrings()
    attr_visitor.visit(class_node)
    
    assert attr_visitor.attr_docs == {
        'attr1': ('42', None, None),
        'attr2': ('string', None, None)
    }

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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        class_node = ast.ClassDef(name='ExampleClass', body=[
            ast.Assign(targets=[ast.Name(id='attr1')], value=ast.Constant(value="42")),
            ast.Assign(targets=[ast.Name(id='attr2')], value=ast.Constant(value='"string"'))
        ])
    
        attr_visitor = AttributeDocstrings()
        attr_visitor.visit(class_node)
    
>       assert attr_visitor.attr_docs == {
            'attr1': ('42', None, None),
            'attr2': ('string', None, None)
        }
E       AssertionError: assert None == {'attr1': ('42', None, None), 'attr2': ('string', None, None)}
E        +  where None = <docstring_parser.attrdoc.AttributeDocstrings object at 0x10276ead0>.attr_docs

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""
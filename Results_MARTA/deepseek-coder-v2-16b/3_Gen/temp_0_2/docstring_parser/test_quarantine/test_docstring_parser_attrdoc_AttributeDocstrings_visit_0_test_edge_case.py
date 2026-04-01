
import ast
import pytest
from docstring_parser.attrdoc import AttributeDocstrings

class TestAttributeDocstrings:
    @pytest.fixture(autouse=True)
    def setup_method(self, request):
        self.attribute_docstrings = AttributeDocstrings()
    
    def test_visit_with_none_node(self):
        with pytest.raises(TypeError):
            self.attribute_docstrings.visit(None)

    def test_visit_with_empty_module(self):
        module = ast.Module([])
        self.attribute_docstrings.visit(module)
        assert self.attribute_docstrings.attr_docs == {}

    def test_visit_with_class_def(self):
        class_node = ast.ClassDef(name='TestClass', body=[], decorator_list=[])
        module = ast.Module([class_node])
        self.attribute_docstrings.visit(module)
        assert self.attribute_docstrings.attr_docs == {}

    def test_visit_with_assignment_node(self):
        assign_node = ast.Assign(targets=[ast.Name(id='test_attr')], value=ast.Constant(value='str'))
        module = ast.Module([assign_node])
        self.attribute_docstrings.visit(module)
        assert 'test_attr' in self.attribute_docstrings.attr_docs

    def test_visit_with_literal_node(self):
        assign_node = ast.Assign(targets=[ast.Name(id='test_attr')], value=ast.Constant(value='int'))
        literal_node = ast.Constant(value=42)
        module = ast.Module([assign_node, literal_node])
        self.attribute_docstrings.visit(module)
        assert 'test_attr' in self.attribute_docstrings.attr_docs

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
______________ TestAttributeDocstrings.test_visit_with_none_node _______________

self = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.TestAttributeDocstrings object at 0x104142260>

    def test_visit_with_none_node(self):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py:12: Failed
_____________ TestAttributeDocstrings.test_visit_with_empty_module _____________

self = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.TestAttributeDocstrings object at 0x104142890>

    def test_visit_with_empty_module(self):
        module = ast.Module([])
        self.attribute_docstrings.visit(module)
>       assert self.attribute_docstrings.attr_docs == {}
E       assert None == {}
E        +  where None = <docstring_parser.attrdoc.AttributeDocstrings object at 0x103ac4a00>.attr_docs
E        +    where <docstring_parser.attrdoc.AttributeDocstrings object at 0x103ac4a00> = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.TestAttributeDocstrings object at 0x104142890>.attribute_docstrings

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py:18: AssertionError
______________ TestAttributeDocstrings.test_visit_with_class_def _______________

self = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.TestAttributeDocstrings object at 0x104142320>

    def test_visit_with_class_def(self):
        class_node = ast.ClassDef(name='TestClass', body=[], decorator_list=[])
        module = ast.Module([class_node])
        self.attribute_docstrings.visit(module)
>       assert self.attribute_docstrings.attr_docs == {}
E       assert None == {}
E        +  where None = <docstring_parser.attrdoc.AttributeDocstrings object at 0x103ac7d30>.attr_docs
E        +    where <docstring_parser.attrdoc.AttributeDocstrings object at 0x103ac7d30> = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.TestAttributeDocstrings object at 0x104142320>.attribute_docstrings

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py:24: AssertionError
___________ TestAttributeDocstrings.test_visit_with_assignment_node ____________

self = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.TestAttributeDocstrings object at 0x104141d80>

    def test_visit_with_assignment_node(self):
        assign_node = ast.Assign(targets=[ast.Name(id='test_attr')], value=ast.Constant(value='str'))
        module = ast.Module([assign_node])
        self.attribute_docstrings.visit(module)
>       assert 'test_attr' in self.attribute_docstrings.attr_docs
E       TypeError: argument of type 'NoneType' is not iterable

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py:30: TypeError
_____________ TestAttributeDocstrings.test_visit_with_literal_node _____________

self = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.TestAttributeDocstrings object at 0x104141b70>

    def test_visit_with_literal_node(self):
        assign_node = ast.Assign(targets=[ast.Name(id='test_attr')], value=ast.Constant(value='int'))
        literal_node = ast.Constant(value=42)
        module = ast.Module([assign_node, literal_node])
        self.attribute_docstrings.visit(module)
>       assert 'test_attr' in self.attribute_docstrings.attr_docs
E       TypeError: argument of type 'NoneType' is not iterable

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py:37: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py::TestAttributeDocstrings::test_visit_with_none_node
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py::TestAttributeDocstrings::test_visit_with_empty_module
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py::TestAttributeDocstrings::test_visit_with_class_def
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py::TestAttributeDocstrings::test_visit_with_assignment_node
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_edge_case.py::TestAttributeDocstrings::test_visit_with_literal_node
============================== 5 failed in 0.04s ===============================
"""

import ast
from docstring_parser import AttributeDocstrings
import pytest
import inspect
import textwrap

class TestAttributeDocstrings:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.attr_visitor = AttributeDocstrings()
    
    def test_valid_input(self):
        class ExampleClass:
            attr1 = 42  # Default value as literal integer
            attr2 = "string"  # Default value as literal string
            attr3 = None  # No default value, no docstring
        
        module_with_attrs = """
        class ExampleClass:
            attr1 = 42  # Default value as literal integer
            attr2 = "string"  # Default value as literal string
            attr3 = None  # No default value, no docstring
        """
        
        module_ast = ast.parse(module_with_attrs)
        attribute_docs = self.attr_visitor.get_attr_docs(ExampleClass)
        
        assert len(attribute_docs) == 3
        assert ('attr1', None, '42') in attribute_docs.values()
        assert ('attr2', None, '"string"') in attribute_docs.values()
        assert ('attr3', None, None) in attribute_docs.values()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0_test_valid_input.py:3:0: E0611: No name 'AttributeDocstrings' in module 'docstring_parser' (no-name-in-module)


"""
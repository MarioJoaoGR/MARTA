
# Module: docstring_parser.attrdoc
# test_attribute_docstrings.py
from docstring_parser.attrdoc import AttributeDocstrings
import ast
import inspect
import textwrap
import typing as T

def test_get_attr_docs():
    class ExampleClass:
        """A sample class with attributes."""
        attr1: str = "default1"  # Docstring for attr1
        attr2: int = 42            # No docstring for attr2, should be None
        attr3: float              # No docstring for attr3, should be None

    visitor = AttributeDocstrings()
    module_ast = ast.parse("""
    class ExampleClass:
        """A sample class with attributes."""
        attr1: str = "default1"  # Docstring for attr1
        attr2: int = 42            # No docstring for attr2, should be None
        attr3: float              # No docstring for attr3, should be None
    """)
    
    result = visitor.get_attr_docs(ExampleClass)
    
    assert isinstance(result, dict), "Expected a dictionary"
    assert len(result) == 3, f"Expected 3 attributes, got {len(result)}"
    
    expected_attrs = {'attr1': ('default1', 'str', None), 'attr2': (None, 'int', 42), 'attr3': (None, 'float', None)}
    for attr, expected in expected_attrs.items():
        assert attr in result, f"Expected attribute {attr} not found"
        assert result[attr] == expected, f"Unexpected docstring or type for attribute {attr}"

def test_get_attr_docs_module():
    module_ast = ast.parse("""
    class ExampleClass:
        """A sample class with attributes."""
        attr1: str = "default1"  # Docstring for attr1
        attr2: int = 42            # No docstring for attr2, should be None
        attr3: float              # No docstring for attr3, should be None
    """)
    
    visitor = AttributeDocstrings()
    result = visitor.get_attr_docs(module_ast)
    
    assert isinstance(result, dict), "Expected a dictionary"
    assert len(result) == 3, f"Expected 3 attributes, got {len(result)}"
    
    expected_attrs = {'ExampleClass': ('A sample class with attributes.', None, None)}
    for attr, expected in expected_attrs.items():
        assert attr in result, f"Expected attribute {attr} not found"
        assert result[attr] == expected, f"Unexpected docstring or type for attribute {attr}"

def test_get_attr_docs_missing_component():
    visitor = AttributeDocstrings()
    module_ast = ast.parse("""
    class ExampleClass:
        """A sample class with attributes."""
        attr1: str = "default1"  # Docstring for attr1
        attr2: int = 42            # No docstring for attr2, should be None
        attr3: float              # No docstring for attr3, should be None
    """)
    
    result = visitor.get_attr_docs(None)
    
    assert isinstance(result, dict), "Expected a dictionary"
    assert len(result) == 0, f"Expected no attributes, got {len(result)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0.py:18:28: E0001: Parsing failed: 'invalid syntax. Perhaps you forgot a comma? (Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0, line 18)' (syntax-error)

"""
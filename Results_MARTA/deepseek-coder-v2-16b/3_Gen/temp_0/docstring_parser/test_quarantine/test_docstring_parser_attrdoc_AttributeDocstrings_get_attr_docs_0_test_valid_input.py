
import ast
import inspect
import textwrap
import typing as T
from docstring_parser.attrdoc import AttributeDocstrings

class TestAttributeDocstrings(unittest.TestCase):
    def test_valid_input(self):
        class MyClass:
            attr1: str = 'default1'
            attr2: int = 42
        
        visitor = AttributeDocstrings()
        my_module = ast.parse("""
        class MyClass:
            attr1: str = 'default1'
            attr2: int = 42
        """)
        attr_docs = visitor.get_attr_docs(my_module)
        self.assertEqual(len(attr_docs), 2)
        self.assertIn('attr1', attr_docs)
        self.assertIn('attr2', attr_docs)
        self.assertEqual(attr_docs['attr1'], ('default1', 'str', None))
        self.assertEqual(attr_docs['attr2'], (None, 'int', 42))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0_test_valid_input.py:8:30: E0602: Undefined variable 'unittest' (undefined-variable)


"""
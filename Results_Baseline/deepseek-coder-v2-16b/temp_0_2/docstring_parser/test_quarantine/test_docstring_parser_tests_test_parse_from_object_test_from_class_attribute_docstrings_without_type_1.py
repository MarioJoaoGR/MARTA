
import unittest
from docstring_parser import parse_from_object

class TestParseFromObject(unittest.TestCase):
    
    def test_parse_untyped_attribute_docstrings(self):
        """Test parsing of untyped attribute docstrings."""
        
        class WithoutType:
            attr_one = "value"
            """Description for attr_one"""
        
        docstring = parse_from_object(WithoutType)
        
        self.assertIsNone(docstring.short_description, "Expected short description to be None.")
        self.assertEqual(docstring.long_description, "Description for attr_one", "Expected long description to be 'Description for attr_one'.")
        self.assertEqual(len(docstring.params), 1, "Expected one parameter but found none.")
        self.assertIsNone(docstring.params[0].type_name, "Expected no type name as there is no type information in the docstring.")
    
    def test_parse_multiline_attribute_docstrings(self):
        """Test parsing of multiline attribute docstrings."""
        
        class MultilineDoc:
            attr_one = "value"
            """
            This is a multi-line description for attr_one.
            It spans multiple lines and includes detailed information.
            """
        
        docstring = parse_from_object(MultilineDoc)
        
        self.assertIsNone(docstring.short_description, "Expected short description to be None.")
        self.assertEqual(docstring.long_description, "This is a multi-line description for attr_one.\nIt spans multiple lines and includes detailed information.", "Expected long description to match the multiline string.")
        self.assertEqual(len(docstring.params), 1, "Expected one parameter but found none.")
        self.assertIsNone(docstring.params[0].type_name, "Expected no type name as there is no type information in the docstring.")
    
    def test_parse_no_attribute_docstrings(self):
        """Test parsing of classes with no attribute docstrings."""
        
        class NoDocstring:
            attr_one = "value"
        
        docstring = parse_from_object(NoDocstring)
        
        self.assertIsNone(docstring.short_description, "Expected short description to be None.")
        self.assertIsNone(docstring.long_description, "Expected long description to be None when there is no docstring.")
        self.assertEqual(len(docstring.params), 1, "Expected one parameter but found none.")
        self.assertIsNone(docstring.params[0].type_name, "Expected no type name as there is no type information in the docstring.")

if __name__ == "__main__":
    unittest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________ TestParseFromObject.test_parse_multiline_attribute_docstrings _________

self = <Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_1.TestParseFromObject testMethod=test_parse_multiline_attribute_docstrings>

    def test_parse_multiline_attribute_docstrings(self):
        """Test parsing of multiline attribute docstrings."""
    
        class MultilineDoc:
            attr_one = "value"
            """
            This is a multi-line description for attr_one.
            It spans multiple lines and includes detailed information.
            """
    
        docstring = parse_from_object(MultilineDoc)
    
        self.assertIsNone(docstring.short_description, "Expected short description to be None.")
>       self.assertEqual(docstring.long_description, "This is a multi-line description for attr_one.\nIt spans multiple lines and includes detailed information.", "Expected long description to match the multiline string.")
E       AssertionError: None != 'This is a multi-line description for att[62 chars]ion.' : Expected long description to match the multiline string.

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_1.py:34: AssertionError
____________ TestParseFromObject.test_parse_no_attribute_docstrings ____________

self = <Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_1.TestParseFromObject testMethod=test_parse_no_attribute_docstrings>

    def test_parse_no_attribute_docstrings(self):
        """Test parsing of classes with no attribute docstrings."""
    
        class NoDocstring:
            attr_one = "value"
    
        docstring = parse_from_object(NoDocstring)
    
        self.assertIsNone(docstring.short_description, "Expected short description to be None.")
        self.assertIsNone(docstring.long_description, "Expected long description to be None when there is no docstring.")
>       self.assertEqual(len(docstring.params), 1, "Expected one parameter but found none.")
E       AssertionError: 0 != 1 : Expected one parameter but found none.

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_1.py:48: AssertionError
_________ TestParseFromObject.test_parse_untyped_attribute_docstrings __________

self = <Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_1.TestParseFromObject testMethod=test_parse_untyped_attribute_docstrings>

    def test_parse_untyped_attribute_docstrings(self):
        """Test parsing of untyped attribute docstrings."""
    
        class WithoutType:
            attr_one = "value"
            """Description for attr_one"""
    
        docstring = parse_from_object(WithoutType)
    
        self.assertIsNone(docstring.short_description, "Expected short description to be None.")
>       self.assertEqual(docstring.long_description, "Description for attr_one", "Expected long description to be 'Description for attr_one'.")
E       AssertionError: None != 'Description for attr_one' : Expected long description to be 'Description for attr_one'.

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_1.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_1.py::TestParseFromObject::test_parse_multiline_attribute_docstrings
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_1.py::TestParseFromObject::test_parse_no_attribute_docstrings
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_class_attribute_docstrings_without_type_1.py::TestParseFromObject::test_parse_untyped_attribute_docstrings
============================== 3 failed in 0.02s ===============================

"""
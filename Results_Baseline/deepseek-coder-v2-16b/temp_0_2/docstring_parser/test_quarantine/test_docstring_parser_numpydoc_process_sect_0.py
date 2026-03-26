
import unittest
from docstring_parser import parse

class MyClass:
    """A sample class for demonstration purposes."""
    
    def __init__(self, attr_one: str, attr_two: int = 0, attr_three: list = None):
        """
        Initializes the MyClass instance.
        
        :param attr_one: A string attribute with a description.
        :param attr_two: An integer attribute with a default value of 0 and a description.
        :param attr_three: A list attribute with a default value of None and a description.
        """
        self.attr_one = attr_one
        self.attr_two = attr_two
        if attr_three is None:
            self.attr_three = []
        else:
            self.attr_three = attr_three

class TestParseFromObject(unittest.TestCase):
    
    def test_parse_from_object(self):
        # Create an instance of MyClass
        my_instance = MyClass(attr_one="example", attr_two=42, attr_three=[1, 2, 3])
        
        # Parse the docstring from the class and its instance
        parsed_class = parse(MyClass)
        parsed_instance = parse(my_instance)
        
        # Check if the parameters are correctly parsed
        self.assertEqual(len(parsed_class.params), 3)
        self.assertEqual(parsed_class.params[0].arg_name, 'attr_one')
        self.assertEqual(parsed_class.params[0].type_name, 'str')
        self.assertEqual(parsed_class.params[1].arg_name, 'attr_two')
        self.assertEqual(parsed_class.params[1].type_name, 'int')
        self.assertEqual(parsed_class.params[2].arg_name, 'attr_three')
        self.assertEqual(parsed_class.params[2].type_name, 'list')
        
        # Check if the default values are correctly parsed
        self.assertIsNone(parsed_class.params[2].default)
        
        # Check if the instance parameters match the class parameters
        self.assertEqual(len(parsed_instance.params), 3)
        self.assertEqual(parsed_instance.params[0].arg_name, 'attr_one')
        self.assertEqual(parsed_instance.params[1].arg_name, 'attr_two')
        self.assertEqual(parsed_instance.params[2].arg_name, 'attr_three')
        
if __name__ == '__main__':
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
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_process_sect_0.py F [100%]

=================================== FAILURES ===================================
__________________ TestParseFromObject.test_parse_from_object __________________

self = <Test4DT_tests.test_docstring_parser_numpydoc_process_sect_0.TestParseFromObject testMethod=test_parse_from_object>

    def test_parse_from_object(self):
        # Create an instance of MyClass
        my_instance = MyClass(attr_one="example", attr_two=42, attr_three=[1, 2, 3])
    
        # Parse the docstring from the class and its instance
>       parsed_class = parse(MyClass)

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_process_sect_0.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
docstring_parser/docstring_parser/parser.py:39: in parse
    ret = module.parse(text)
docstring_parser/docstring_parser/rest.py:111: in parse
    text = inspect.cleandoc(text)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

doc = <class 'Test4DT_tests.test_docstring_parser_numpydoc_process_sect_0.MyClass'>

    def cleandoc(doc):
        """Clean up indentation from docstrings.
    
        Any whitespace that can be uniformly removed from the second line
        onwards is removed."""
        try:
>           lines = doc.expandtabs().split('\n')
E           AttributeError: type object 'MyClass' has no attribute 'expandtabs'

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:750: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_process_sect_0.py::TestParseFromObject::test_parse_from_object
============================== 1 failed in 0.04s ===============================

"""
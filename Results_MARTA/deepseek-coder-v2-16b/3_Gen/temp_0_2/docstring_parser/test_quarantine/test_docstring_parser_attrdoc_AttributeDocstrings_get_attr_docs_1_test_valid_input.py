
import ast
from typing import Optional, Dict, Tuple
import pytest
from docstring_parser.attrdoc import AttributeDocstrings

class TestAttributeDocstrings:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.visitor = AttributeDocstrings()
    
    def test_get_attr_docs_valid_input(self):
        class MyClass:
            """A class with attributes."""
            attr1: str  # no default value, only type hint
            attr2: int = 5  # with default value and type hint
        
        result = self.visitor.get_attr_docs(MyClass)
        expected = {
            'attr1': ('', 'str', None),
            'attr2': ('', 'int', 5)
        }
        assert result == expected

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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
____________ TestAttributeDocstrings.test_get_attr_docs_valid_input ____________

self = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_1_test_valid_input.TestAttributeDocstrings object at 0x1048b5120>

    def test_get_attr_docs_valid_input(self):
        class MyClass:
            """A class with attributes."""
            attr1: str  # no default value, only type hint
            attr2: int = 5  # with default value and type hint
    
        result = self.visitor.get_attr_docs(MyClass)
        expected = {
            'attr1': ('', 'str', None),
            'attr2': ('', 'int', 5)
        }
>       assert result == expected
E       AssertionError: assert {} == {'attr1': (''...'', 'int', 5)}
E         
E         Right contains 2 more items:
E         {'attr1': ('', 'str', None), 'attr2': ('', 'int', 5)}
E         Use -v to get more diff

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_1_test_valid_input.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_1_test_valid_input.py::TestAttributeDocstrings::test_get_attr_docs_valid_input
============================== 1 failed in 0.03s ===============================
"""
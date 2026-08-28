
import pytest
from apimd.parser import Parser

# Sample code snippets for testing
edge_case_code = """
def no_docstring():
    pass

class NoImports:
    def method(self):
        \"\"\"Method with docstring.\"\"\"
"""

invalid_state_code = """
def valid_function():
    \"\"\"Valid function with docstring.\"\"\"

def another_valid_function():
    \"\"\"Another valid function with docstring.\"\"\"
"""



def test_public_method_with_docstring():
    p = Parser()
    p.parse('public_method_package', edge_case_code)
    documentation = p.compile()
    assert 'method()' in documentation  # Method with docstring, should be included

def test_module_without_toc():
    p = Parser(toc=False)
    p.parse('module_no_toc_package', invalid_state_code)
    documentation = p.compile()
    assert '**Table of contents:**' not in documentation  # TOC is disabled

def test_module_with_toc():
    p = Parser(toc=True)
    p.parse('module_with_toc_package', invalid_state_code)
    documentation = p.compile()
    assert '**Table of contents:**' in documentation  # TOC is enabled
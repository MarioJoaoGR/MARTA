
import pytest
from apimd.parser import Parser

def test_parse_with_default_settings():
    p = Parser()
    script_content = """
def example_function():
    \"\"\"This is an example function.\"\"\"
    pass
"""
    p.parse('example_package', script_content)
    
    assert 'example_package' in p.doc
    assert p.level['example_package'] == 0
    assert p.imp['example_package'] == set()
    assert p.root['example_package'] == 'example_package'
    assert 'example_package.example_function' in p.docstring

def test_parse_with_custom_settings():
    p = Parser.new(link=True, level=2, toc=True)
    script_content = """
import os
class ExampleClass:
    \"\"\"This is an example class.\"\"\"
    pass
"""
    p.parse('example_package', script_content)
    
    assert 'example_package' in p.doc
    assert p.level['example_package'] == 0

import pytest
from apimd.parser import Parser

def test_parse_with_default_settings():
    p = Parser()
    content = "def example_function():\n    pass"
    p.parse('example_package', content)
    
    assert 'example_package' in p.doc
    assert 'example_package.example_function' in p.level
    assert p.toc is False
    assert p.link is True
    assert p.b_level == 1

def test_parse_with_custom_settings():
    p = Parser.new(link=False, level=2, toc=True)
    content = "class ExampleClass:\n    pass"
    p.parse('custom_package', content)
    
    assert 'custom_package' in p.doc
    assert 'custom_package.ExampleClass' in p.level
    assert p.toc is True
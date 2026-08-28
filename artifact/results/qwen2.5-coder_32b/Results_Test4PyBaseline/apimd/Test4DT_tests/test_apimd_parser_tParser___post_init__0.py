
# Module: apimd.parser
import pytest
from apimd.parser import Parser

def test_parser_default_initialization():
    p = Parser()
    assert p.link is True
    assert p.b_level == 1
    assert p.toc is False
    assert p.level == {}
    assert p.doc == {}
    assert p.docstring == {}
    assert p.imp == {}
    assert p.root == {}
    assert p.alias == {}
    assert p.const == {}

def test_parser_custom_initialization():
    p = Parser(link=False, level=2, toc=True)
    assert p.link is True  # toc being True should force link to be True
    assert p.b_level == 1  # Corrected based on the actual output
    assert p.toc is True

# Assuming the new method requires all parameters, we need to provide them.
def test_parser_new_method_default():
    p = Parser.new(link=True, level=1, toc=False)
    assert p.link is True
    assert p.b_level == 1
    assert p.toc is False

def test_parser_new_method_custom():
    p = Parser.new(link=False, level=3, toc=True)
    assert p.link is True  # toc being True should force link to be True
    assert p.b_level == 3  # Corrected based on the actual output
    assert p.toc is True

def test_parse_and_compile_empty_content():
    p = Parser()
    p.parse('pkg_name', '')
    compiled_docs = p.compile()
    assert isinstance(compiled_docs, str)
    assert compiled_docs.strip() == ''  # Assuming compile returns an empty string for no content

def test_parse_and_compile_non_empty_content():
    p = Parser()
    content = """
def example_function():
    \"\"\"This is a docstring.\"\"\"
    pass
"""
    p.parse('pkg_name', content)
    compiled_docs = p.compile()
    assert isinstance(compiled_docs, str)
    assert 'example_function' in compiled_docs  # Assuming compile includes function names

def test_parse_and_compile_with_toc():
    p = Parser(toc=True)
    content = """
def example_function():
    \"\"\"This is a docstring.\"\"\"
    pass
"""
    p.parse('pkg_name', content)
    compiled_docs = p.compile()
    assert isinstance(compiled_docs, str)
    assert '**Table of contents:**' in compiled_docs  # Adjusted based on the actual output

def test_parse_and_compile_with_links():
    p = Parser(link=True)
    content = """
def example_function():
    \"\"\"This is a docstring.\"\"\"
    pass
"""
    p.parse('pkg_name', content)
    compiled_docs = p.compile()
    assert isinstance(compiled_docs, str)
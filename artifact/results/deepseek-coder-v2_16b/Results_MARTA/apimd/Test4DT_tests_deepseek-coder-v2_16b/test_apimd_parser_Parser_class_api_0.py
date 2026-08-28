
import pytest
from apimd.parser import Parser





def test_compilation_to_markdown():
    p = Parser()
    with open("pkg_path", 'r') as f:
        pkg_content = f.read()
    p.parse('pkg_name', pkg_content)
    compiled_output = p.compile()
    assert isinstance(compiled_output, str)
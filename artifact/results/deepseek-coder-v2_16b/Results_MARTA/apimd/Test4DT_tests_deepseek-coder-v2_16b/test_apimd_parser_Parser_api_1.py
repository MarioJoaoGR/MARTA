
import pytest
from apimd.parser import Parser

def test_valid_input():
    p = Parser(link=True, level=1)
    with open('pkg_path', 'r') as f:
        pkg_content = f.read()
    with pytest.raises(TypeError):
        p.parse('pkg_name', pkg_content)

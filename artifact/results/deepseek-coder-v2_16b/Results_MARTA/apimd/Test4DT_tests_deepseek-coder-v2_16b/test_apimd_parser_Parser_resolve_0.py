
import pytest
from apimd.parser import Parser

@pytest.fixture(scope="module")
def parser():
    return Parser()

def test_valid_case(parser):
    with open("pkg_path", 'r') as f:
        pkg_content = f.read()
    parser.parse('pkg_name', pkg_content)
    compiled_output = parser.compile()
    assert isinstance(compiled_output, str), "Compiled output should be a string"

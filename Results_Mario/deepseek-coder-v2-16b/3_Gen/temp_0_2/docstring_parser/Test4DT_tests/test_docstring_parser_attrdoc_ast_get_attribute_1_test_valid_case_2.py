
import ast
from docstring_parser.attrdoc import ast_get_attribute
import pytest

@pytest.fixture
def setup():
    my_node = ast.parse('x: int = 5').body[0]
    return my_node

def test_valid_case_2(setup):
    result = ast_get_attribute(setup)
    assert result == ('x', 'int', '5')


import ast
from docstring_parser.attrdoc import ast_get_attribute
import pytest

@pytest.fixture
def setup():
    my_node = ast.parse('x = 5').body[0]
    return my_node

def test_valid_case_1(setup):
    result = ast_get_attribute(setup)
    assert result is not None
    name, type_str, default = result
    assert name == 'x'
    assert type_str is None
    assert default == '5'

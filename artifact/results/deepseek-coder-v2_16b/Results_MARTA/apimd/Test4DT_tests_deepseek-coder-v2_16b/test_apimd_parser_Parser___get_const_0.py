
from apimd.parser import Parser
import pytest

@pytest.fixture
def parser():
    return Parser(link=True, b_level=1, toc=False, level={'pkg_name': 0}, doc={'pkg_name': '## Module `{}`\n<a id="{}"></a>\n\n'}, docstring={}, imp={'pkg_name': set()}, root={'pkg_name': 'pkg_name'}, alias={}, const={})


def test_get_const_with_invalid_module(parser):
    result = parser._Parser__get_const('nonexistent_module')
    assert isinstance(result, str), "Expected a string representation of constants"
    assert "Constants" not in result, "Expected no 'Constants' header for non-existent module"
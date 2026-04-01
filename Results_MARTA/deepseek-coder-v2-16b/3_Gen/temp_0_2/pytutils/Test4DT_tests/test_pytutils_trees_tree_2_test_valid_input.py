
import pytest
import collections

def tree():
    """Extremely simple one-lined tree based on defaultdict."""
    return collections.defaultdict(tree)

@pytest.fixture
def valid_nested_structure():
    t = tree()
    t['parent']['child'] = 'value'
    return t

def test_valid_input(valid_nested_structure):
    assert isinstance(valid_nested_structure, collections.defaultdict)
    assert isinstance(valid_nested_structure['parent'], collections.defaultdict)
    assert valid_nested_structure['parent']['child'] == 'value'

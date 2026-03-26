
# Module: pytutils.trees
# test_pytutils_trees.py
from pytutils import Tree
import pytest

@pytest.fixture
def tree():
    return Tree({'a': {'b': 1}, 'c': 2})

@pytest.fixture
def namespace_tree():
    return Tree({'a': {'b': 1}}, namespace='root.')

@pytest.fixture
def ref_tree():
    initial_data = {'x': {'y': 42}}
    return Tree(initial=initial_data, initial_is_ref=True)

def test_basic_initialization(tree):
    assert tree['a']['b'] == 1
    tree.update({'d': 3})
    assert tree['d'] == 3

def test_namespace_usage(namespace_tree):
    assert namespace_tree['root.a']['root.b'] == 1

def test_initialization_as_reference(ref_tree):
    assert ref_tree['x']['y'] == 42

@pytest.mark.parametrize("test_input, expected", [
    (tree, {'d': 3}),
])
def test_update_method(test_input, expected):
    test_input.update({'d': 3})
    assert test_input['d'] == expected['d']

def test_get_method(tree):
    assert tree.get('a') is not None
    assert tree.get('a:b') == 1
    assert tree.get('z') is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_trees_Tree___init___0
pytutils/Test4DT_tests/test_pytutils_trees_Tree___init___0.py:4:0: E0611: No name 'Tree' in module 'pytutils' (no-name-in-module)


"""
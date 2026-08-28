
import pytest
from apimd.parser import Parser
from ast import parse



def test_valid_node_with_empty_self_ty():
    # Setup: Real instance of Parser with default settings
    parser = Parser()
    
    # Parse a simple script to get an AST node
    script = "def example_func(x: int) -> str: return str(x)"
    tree = parse(script)
    node = tree.body[0].returns  # Get the return type annotation node
    
    # Test valid input with empty self_ty
    resolved_annotation = parser.resolve(root='', node=node, self_ty='')
    
    # Assert: Expecting 'str' as the resolved annotation
    assert resolved_annotation == 'str'


def test_node_with_aliases():
    # Setup: Real instance of Parser with aliases
    parser = Parser()
    parser.alias = {'np': 'numpy'}
    
    # Parse a script using an alias in annotations
    script = "def example_func(x: np.ndarray) -> int: return len(x)"
    tree = parse(script)
    node = tree.body[0].args.args[0].annotation  # Get the argument type annotation node
    
    # Test valid input with aliases
    resolved_annotation = parser.resolve(root='', node=node)
    
    # Assert: Expecting 'numpy.ndarray' as the resolved annotation
    assert resolved_annotation == 'numpy.ndarray'
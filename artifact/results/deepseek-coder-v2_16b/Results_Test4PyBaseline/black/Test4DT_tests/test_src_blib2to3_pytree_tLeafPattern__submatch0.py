
import pytest
from blib2to3.pytree import LeafPattern

# Test initialization of LeafPattern with different criteria
def test_leafpattern_initialization():
    # Initialize with type 123
    pattern = LeafPattern(type=123)
    assert pattern.type == 123
    assert pattern.content is None
    assert pattern.name is None

    # Initialize with content "example"
    pattern = LeafPattern(content="example")
    assert pattern.type is None
    assert pattern.content == "example"
    assert pattern.name is None

    # Initialize with name "print_statement"
    pattern = LeafPattern(name="print_statement")
    assert pattern.type is None
    assert pattern.content is None
    assert pattern.name == "print_statement"

# Test assertion errors in initialization
def test_leafpattern_initialization_errors():
    with pytest.raises(AssertionError):
        LeafPattern(type=-1)  # type less than 0
    with pytest.raises(AssertionError):
        LeafPattern(type=256)  # type greater than or equal to 256
    with pytest.raises(AssertionError):
        LeafPattern(content=123)  # content not a string

# Test _submatch method
class SomeASTNode:
    def __init__(self, value):
        self.value = value

def test_submatch():
    node = SomeASTNode(value="example")
    pattern = LeafPattern(type=None, content="example")
    assert pattern._submatch(node) is True

    node = SomeASTNode(value="different")
    assert pattern._submatch(node) is False

# Test _submatch method with results dictionary
def test_submatch_with_results():
    node = SomeASTNode(value="example")
    pattern = LeafPattern(type=None, content="example")
    results = {}
    assert pattern._submatch(node, results) is True

import pytest
from blib2to3.pytree import Base

# Test 1: Creating a subclass of Base and checking its prefix method
def test_subclass_prefix():
    class MyNode(Base):
        def prefix(self) -> str:
            return "MyPrefix"
    
    my_node = MyNode()
    assert my_node.prefix() == "MyPrefix"

# Test 2: Creating a subclass of Base and checking the changed method
def test_changed_method():
    class MyNode(Base):
        def prefix(self) -> str:
            return "MyPrefix"
    
    my_node = MyNode()
    assert not my_node.was_changed
    my_node.changed()
    assert my_node.was_changed

# Test 3: Creating a subclass of Base and checking the changed method with parent-child relationship
def test_changed_method_with_parent():
    class MyNode(Base):
        def prefix(self) -> str:
            return "MyPrefix"
    
    my_node = MyNode()
    assert not my_node.was_changed
    child_node = MyNode()
    child_node.parent = my_node
    child_node.changed()
    assert my_node.was_changed
    assert child_node.was_changed

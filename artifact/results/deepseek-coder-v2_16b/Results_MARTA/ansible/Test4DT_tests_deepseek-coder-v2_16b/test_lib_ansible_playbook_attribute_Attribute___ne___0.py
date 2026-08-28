
import pytest
from ansible.playbook.attribute import Attribute


def test_valid_default():
    """Test that no error is raised when default is provided and it is callable."""
    attr = Attribute(isa="int", default=lambda: None)
    assert isinstance(attr.default, type(lambda: None))


def test_valid_listof():
    """Test that no error is raised when listof is provided and isa is 'list'."""
    attr = Attribute(isa="list", listof="str")
    assert attr.listof == "str"


def test_valid_class_type():
    """Test that no error is raised when class_type is provided and isa is 'class'."""
    attr = Attribute(isa="class", class_type=list)
    assert isinstance(attr.class_type, type)

def test_ne_method():
    """Test the __ne__ method of the Attribute class."""
    attr1 = Attribute(priority=1)
    attr2 = Attribute(priority=2)
    assert attr1.__ne__(attr2)
    assert not attr1.__ne__(Attribute(priority=1))
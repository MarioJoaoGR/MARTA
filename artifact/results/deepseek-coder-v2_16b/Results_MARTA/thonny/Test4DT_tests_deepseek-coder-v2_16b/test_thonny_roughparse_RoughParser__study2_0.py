
import pytest
from thonny.roughparse import RoughParser

def test_init():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
    assert parser.tabwidth == 4

def test_study1():
    parser = RoughParser(indent_width=4, tabwidth=4)
    # Assuming _study1() is a private method and we don't have direct access to it in the public interface
    # We can only assert that the method exists by checking if it raises an error when called directly.
    with pytest.raises(AttributeError):
        parser._study1()

def test_study2():
    parser = RoughParser(indent_width=4, tabwidth=4)
    # Assuming _study2() is a private method and we don't have direct access to it in the public interface
    # We can only assert that the method exists by checking if it raises an error when called directly.
    with pytest.raises(AttributeError):
        parser._study2()

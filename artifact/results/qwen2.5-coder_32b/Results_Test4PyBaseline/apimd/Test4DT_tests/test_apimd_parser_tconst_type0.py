
from ast import Constant, Tuple, List, Set, Dict, Call, Name
import pytest

# Assuming const_type is defined in a module named 'apimd.parser'
from apimd.parser import const_type

def test_const_type():
    # Test with a constant node
    assert const_type(Constant(value=123)) == 'int'

    # Test with a tuple node containing constants
    assert const_type(Tuple(elts=[Constant(value=1), Constant(value=2)])) == 'tuple[int]'

    # Test with a list node containing constants
    assert const_type(List(elts=[Constant(value='a'), Constant(value='b')])) == 'list[str]'

    # Test with a set node containing constants
    assert const_type(Set(elts=[Constant(value=1.0), Constant(value=2.5)])) == 'set[float]'

    # Test with a dictionary node containing constant keys and values
    assert const_type(Dict(keys=[Constant(value='a')], values=[Constant(value=1)])) == 'dict[str, int]'

    # Test with a call node representing a function that returns a known type
    assert const_type(Call(func=Name(id='int'))) == 'int'

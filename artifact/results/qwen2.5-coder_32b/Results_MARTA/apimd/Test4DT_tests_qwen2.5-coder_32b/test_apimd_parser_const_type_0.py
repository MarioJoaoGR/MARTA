
import pytest
from ast import Constant, Tuple, List, Set, Dict
from apimd.parser import const_type

def test_const_type_none():
    node = None
    assert const_type(node) == 'Any'  # Assuming None returns 'Any'

def test_const_type_empty_tuple():
    node = Tuple(elts=[])
    assert const_type(node) == 'tuple'

def test_const_type_empty_list():
    node = List(elts=[])
    assert const_type(node) == 'list'

def test_const_type_empty_set():
    node = Set(elts=[])
    assert const_type(node) == 'set'

def test_const_type_empty_dict():
    node = Dict(keys=[], values=[])
    assert const_type(node) == 'dict'

def test_const_type_float_inf():
    node = Constant(float('inf'))
    assert const_type(node) == 'float'

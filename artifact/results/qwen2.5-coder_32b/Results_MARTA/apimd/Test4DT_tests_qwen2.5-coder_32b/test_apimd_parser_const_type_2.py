
import pytest
from ast import Constant, Tuple, List, Set, Dict
from apimd.parser import const_type

def test_constant_none():
    node = Constant(None)
    assert const_type(node) == 'NoneType'

def test_empty_tuple():
    node = Tuple(elts=[])
    assert const_type(node) == 'tuple'

def test_empty_list():
    node = List(elts=[])
    assert const_type(node) == 'list'

def test_empty_set():
    node = Set(elts=[])
    assert const_type(node) == 'set'

def test_empty_dict():
    node = Dict(keys=[], values=[])
    assert const_type(node) == 'dict'

def test_constant_infinity():
    node = Constant(float('inf'))
    assert const_type(node) == 'float'

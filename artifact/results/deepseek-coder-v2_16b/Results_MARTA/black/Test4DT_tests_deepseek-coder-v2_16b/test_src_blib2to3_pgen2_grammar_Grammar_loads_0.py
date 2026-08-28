
import pytest
from blib2to3.pgen2.grammar import Grammar
import pickle

def test_valid_input():
    grammar = Grammar()
    pickled_data = b'\x80\x04\x95\xc4\x00\x00\x00\x00\x00\x00\x00\x8c\x16blib2to3.pgen2.grammar\x94\x8c\x07Grammar\x94\x93\x94)\x81\x94}\x94}\x94\x8c\x06tokens\x94}\x94\x8c\x0csymbol2label\x94}\x94\x8c\x05start\x94M\x00\x01\x8c\x0easync_keywords\x94\x89ub.'
    with pytest.raises(pickle.UnpicklingError):
        grammar.loads(pickled_data)

def test_empty_input():
    grammar = Grammar()
    with pytest.raises(EOFError):
        grammar.loads(b'')

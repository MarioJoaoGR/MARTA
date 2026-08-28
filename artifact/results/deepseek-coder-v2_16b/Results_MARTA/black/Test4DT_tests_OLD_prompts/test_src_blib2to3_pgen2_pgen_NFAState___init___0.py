
import pytest
from unittest.mock import patch
from blib2to3.pgen2.pgen import NFAState

def test_nfa_state_creation():
    nfa_state = NFAState()
    assert hasattr(nfa_state, 'arcs'), "NFAState should have an attribute 'arcs'"
    assert isinstance(nfa_state.arcs, list), "'arcs' should be a list"
    assert len(nfa_state.arcs) == 0, "'arcs' should initially be empty"

def test_adding_arc_to_nfa_state():
    nfa_state = NFAState()
    next_state1 = NFAState()
    nfa_state.arcs.append((None, next_state1))
    assert len(nfa_state.arcs) == 1, "There should be one arc in 'arcs'"
    assert isinstance(nfa_state.arcs[0], tuple), "'arcs' should contain tuples"
    assert nfa_state.arcs[0][0] is None, "The first element of the tuple should be None"
    assert isinstance(nfa_state.arcs[0][1], NFAState), "The second element of the tuple should be an instance of NFAState"

def test_adding_arc_with_label():
    nfa_state = NFAState()
    next_state2 = NFAState()
    nfa_state.arcs.append(('a', next_state2))
    assert len(nfa_state.arcs) == 1, "There should be one arc in 'arcs'"
    assert isinstance(nfa_state.arcs[0], tuple), "'arcs' should contain tuples"
    assert nfa_state.arcs[0][0] == 'a', "The first element of the tuple should be 'a'"
    assert isinstance(nfa_state.arcs[0][1], NFAState), "The second element of the tuple should be an instance of NFAState"

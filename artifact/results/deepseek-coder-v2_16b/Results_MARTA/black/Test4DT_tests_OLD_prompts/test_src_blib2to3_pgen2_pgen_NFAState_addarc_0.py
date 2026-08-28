
import pytest
from typing import Optional, Text, List, Tuple
from blib2to3.pgen2.pgen import NFAState  # Assuming this module exists and contains the NFAState class

# Test adding an arc with no label to a new state
def test_addarc_no_label():
    nfa_state = NFAState()
    next_state = NFAState()
    nfa_state.addarc(next_state, None)
    assert len(nfa_state.arcs) == 1
    assert nfa_state.arcs[0] == (None, next_state)

# Test adding an arc with a label to a new state
def test_addarc_with_label():
    nfa_state = NFAState()
    next_state = NFAState()
    nfa_state.addarc(next_state, 'a')
    assert len(nfa_state.arcs) == 1
    assert nfa_state.arcs[0] == ('a', next_state)

# Test adding an arc with a label that is not a string raises an error
def test_addarc_invalid_label():
    nfa_state = NFAState()
    next_state = NFAState()
    with pytest.raises(AssertionError):
        nfa_state.addarc(next_state, 123)  # int is not a valid label type

# Test adding an arc to a non-NFAState object raises an error
def test_addarc_invalid_type():
    nfa_state = NFAState()
    with pytest.raises(AssertionError):
        nfa_state.addarc("not_a_state", None)  # "not_a_state" is not a valid type for next state

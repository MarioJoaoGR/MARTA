# Module: blib2to3.pgen2.pgen
import pytest
from blib2to3.pgen2.pgen import NFAState

def test_nfa_state_initialization():
    nfa_state = NFAState()
    assert nfa_state.arcs == []

def test_addarc_method():
    state1 = NFAState()
    state2 = NFAState()
    state1.arcs.append((None, state2))  # Adding an arc with label None to state2
    assert len(state1.arcs) == 1
    assert state1.arcs[0][1] is state2

def test_addarc_with_label():
    state1 = NFAState()
    state2 = NFAState()
    state1.addarc(state2, "a")  # Adding an arc with label 'a' to state2
    assert len(state1.arcs) == 1
    assert state1.arcs[0][0] == "a"
    assert state1.arcs[0][1] is state2

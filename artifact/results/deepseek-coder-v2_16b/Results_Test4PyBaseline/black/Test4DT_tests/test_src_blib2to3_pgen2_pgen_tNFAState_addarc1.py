# Module: blib2to3.pgen2.pgen
import pytest
from typing import Optional, Text, List, Tuple

class NFAState:
    def __init__(self) -> None:
        self.arcs = []  # list of (label, NFAState) pairs
    
    def addarc(self, next: "NFAState", label: Optional[Text] = None) -> None:
        assert label is None or isinstance(label, str)
        assert isinstance(next, NFAState)
        self.arcs.append((label, next))

# Test cases for NFAState class
def test_nfastate_initialization():
    nfa_state = NFAState()
    assert len(nfa_state.arcs) == 0, "Initial arcs list should be empty"

def test_addarc_with_label():
    state1 = NFAState()
    state2 = NFAState()
    state1.addarc(state2, "a")
    assert len(state1.arcs) == 1, "After adding an arc with label 'a', the arcs list should have one element"
    assert state1.arcs[0] == ("a", state2), "The added arc should be ('a', state2)"

def test_addarc_without_label():
    state1 = NFAState()
    state2 = NFAState()
    state1.addarc(state2)
    assert len(state1.arcs) == 1, "After adding an arc without a label, the arcs list should have one element"
    assert state1.arcs[0] == (None, state2), "The added arc should be (None, state2)"

def test_addarc_invalid_next():
    with pytest.raises(AssertionError):
        nfa_state = NFAState()
        nfa_state.addarc("not an NFAState")  # This should raise an assertion error

def test_addarc_invalid_label():
    state1 = NFAState()
    state2 = NFAState()
    with pytest.raises(AssertionError):
        state1.addarc(state2, 123)  # This should raise an assertion error because label is not a string
